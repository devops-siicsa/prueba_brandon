from app import create_app, db
from app.models.core_models import Fabricante
from app.models.audit_models import AuditoriaLog
import time

app = create_app()

with app.app_context():
    print("--- Verificando Auditoría de Fabricante ---")
    
    # 1. Crear Fabricante
    print("Creando Fabricante de prueba...")
    nombre_fab = f"FabTest_{int(time.time())}"
    nuevo_fab = Fabricante(Nombre=nombre_fab, Activo=True)
    db.session.add(nuevo_fab)
    db.session.commit()
    print(f"Fabricante creado con ID: {nuevo_fab.Id}")
    
    # 2. Verificar Log de Creación
    log_crear = AuditoriaLog.query.filter_by(
        TablaAfectada='Fabricantes', 
        RegistroId=nuevo_fab.Id, 
        Accion='CREAR'
    ).first()
    
    if log_crear:
        print("✅ Log de CREACIÓN encontrado.")
        print(f"   Detalle: {log_crear.DetalleCambio}")
    else:
        print("❌ Log de CREACIÓN NO encontrado.")

    # 3. Editar Fabricante (Desactivar)
    print("Desactivando Fabricante...")
    nuevo_fab.Activo = False
    db.session.commit()
    
    # 4. Verificar Log de Edición
    log_editar = AuditoriaLog.query.filter_by(
        TablaAfectada='Fabricantes', 
        RegistroId=nuevo_fab.Id, 
        Accion='EDITAR'
    ).order_by(AuditoriaLog.Fecha.desc()).first()
    
    if log_editar:
        print("✅ Log de EDICIÓN encontrado.")
        print(f"   Campo Afectado: {log_editar.CampoAfectado}")
        print(f"   Valor Antes: {log_editar.ValorAntes}")
        print(f"   Valor Después: {log_editar.ValorDespues}")
    else:
        print("❌ Log de EDICIÓN NO encontrado.")

    # Limpieza
    # db.session.delete(nuevo_fab)
    # db.session.commit()
