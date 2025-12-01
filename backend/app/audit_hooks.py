from sqlalchemy import event, inspect
from sqlalchemy.orm import Session
from app.extensions import db
from app.models.audit_models import AuditoriaLog
from flask import g
from datetime import datetime
import json

def register_audit_hooks(app):
    """
    Registra los eventos de SQLAlchemy para auditoría.
    """
    
    @event.listens_for(Session, 'after_flush')
    def receive_after_flush(session, flush_context):
        """
        Captura cambios después del flush pero antes del commit.
        """
        try:
            for instance in list(session.new):
                if isinstance(instance, AuditoriaLog):
                    continue
                create_log(session, instance, 'CREAR')

            for instance in list(session.dirty):
                if isinstance(instance, AuditoriaLog):
                    continue
                create_log(session, instance, 'EDITAR')

            for instance in list(session.deleted):
                if isinstance(instance, AuditoriaLog):
                    continue
                create_log(session, instance, 'ELIMINAR')
        except Exception as e:
            print(f"Error en receive_after_flush: {e}")

from sqlalchemy import insert

def create_log(session, instance, action):
    try:
        # Evitar recursión: Si la instancia es AuditoriaLog, ignorar
        if isinstance(instance, AuditoriaLog):
            return

        # Obtener usuario actual de manera segura
        user_id = None
        try:
            if hasattr(g, 'current_user') and g.current_user:
                user_id = g.current_user.Id
        except:
            pass 

        table_name = instance.__tablename__
        record_id = None
        
        # Intentar obtener ID
        mapper = inspect(instance).mapper
        if mapper.primary_key:
            pk_attr = mapper.primary_key[0]
            record_id = getattr(instance, pk_attr.name)

        detalle = {}
        campo_afectado = None
        valor_antes = None
        valor_despues = None

        if action == 'EDITAR':
            state = inspect(instance)
            
            # Detectar si es un LOGIN (Solo cambia UltimoLogin y/o IntentosFallidos en Personas)
            is_login_event = False
            if table_name == 'Personas':
                changed_attrs = [attr.key for attr in state.attrs if attr.history.has_changes()]
                # Campos que indican login
                login_fields = {'UltimoLogin', 'IntentosFallidos'}
                # Si todos los campos cambiados son de login
                if changed_attrs and set(changed_attrs).issubset(login_fields):
                    is_login_event = True

            if is_login_event:
                action = 'LOGIN'
                detalle_str = "Inicio de Sesión Exitoso"
                valor_despues = "Login"
                # No procesamos detalle atributo por atributo para login
            else:
                for attr in state.attrs:
                    hist = attr.history
                    if hist.has_changes():
                        old_value = hist.deleted[0] if hist.deleted else None
                        new_value = hist.added[0] if hist.added else None
                        
                        # Ignorar campos de auditoría interna si existen
                        if attr.key in ['UltimoLogin', 'IntentosFallidos', 'BloqueoHasta']:
                            continue

                        detalle[attr.key] = {
                            'antes': str(old_value),
                            'despues': str(new_value)
                        }
                        
                        campo_afectado = attr.key
                        valor_antes = str(old_value)
                        valor_despues = str(new_value)
                
                if not detalle:
                    return 
                    
                detalle_str = json.dumps(detalle, default=str)

        elif action == 'CREAR':
            state = inspect(instance)
            data = {}
            for attr in state.mapper.column_attrs:
                val = getattr(instance, attr.key)
                if val is not None:
                    data[attr.key] = val
            detalle_str = json.dumps(data, default=str)
            valor_despues = "Registro Creado"

        elif action == 'ELIMINAR':
            detalle_str = "Registro Eliminado"
            valor_antes = "Registro Eliminado"

        # Usar Core Insert para evitar problemas con la sesión ORM en el hook
        stmt = insert(AuditoriaLog).values(
            TablaAfectada=table_name,
            RegistroId=record_id,
            Accion=action,
            UsuarioId=user_id,
            Fecha=datetime.now(),
            DetalleCambio=detalle_str,
            CampoAfectado=campo_afectado,
            ValorAntes=valor_antes,
            ValorDespues=valor_despues
        )
        
        # Usar la misma sesión para evitar deadlocks (bloqueos)
        # Al usar Core Insert (stmt), no disparamos eventos ORM recursivos
        session.execute(stmt)
        # No hacemos commit aquí, dejamos que la transacción principal haga commit

    except Exception as e:
        print(f"Error creando log de auditoría: {e}")
