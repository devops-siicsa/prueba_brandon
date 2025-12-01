from app import create_app, db
from app.models.audit_models import AuditoriaLog
from app.models.auth_models import Persona
from app.models.inventory_models import TipoRAM
from flask import g

app = create_app()

# Simular contexto de request
with app.test_request_context('/api/audit/logs'):
    with app.app_context():
        print("--- Verificando Fix y Filtros ---")
        
        # 1. Simular Usuario Logueado
        user = Persona.query.filter_by(Correo='debug_admin@siicsa.com').first()
        if not user:
            print("Usuario de prueba no encontrado, saltando prueba de usuario.")
        else:
            g.current_user = user
            print(f"Usuario actual: {user.Nombre}")

        # 2. Verificar que NO hay recursión al editar campos ignorados (simulación)
        # Modificamos un campo que NO sea de auditoría para ver si genera log
        print("Creando registro para prueba...")
        nuevo = TipoRAM(Nombre="FilterTestRAM")
        db.session.add(nuevo)
        db.session.commit()
        
        print("Editando registro...")
        nuevo.Nombre = "FilterTestRAM_Edited"
        db.session.commit()
        
        # 3. Verificar Log
        log = AuditoriaLog.query.filter_by(TablaAfectada='TiposRAM', RegistroId=nuevo.Id, Accion='EDITAR').first()
        if log:
            print(f"[OK] Log generado: {log.DetalleCambio}")
        else:
            print("[ERROR] Log no generado")

        # 4. Verificar Filtros (Simulación de query)
        # Esto es solo para asegurar que la sintaxis de la query en audit_routes no explota,
        # aunque aquí estamos probando lógica directa, no la ruta.
        # Para probar la ruta, haríamos client.get().
        
        print("Limpiando...")
        db.session.delete(nuevo)
        db.session.commit()
