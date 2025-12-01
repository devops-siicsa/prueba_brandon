from app import create_app, db
from app.models.core_models import Empresa
from app.models.audit_models import AuditoriaLog
import time

app = create_app()

with app.app_context():
    print("--- Verificando Auditoría de Empresa ---")
    
    # 1. Crear Empresa
    print("Creando Empresa de prueba...")
    nit = f"900{int(time.time())}"
    nueva_empresa = Empresa(
        NIT=nit, 
        RazonSocial=f"Empresa Test {nit}", 
        Activo=True,
        EsCliente=False # Proveedor?
    )
    db.session.add(nueva_empresa)
    db.session.commit()
    print(f"Empresa creada con ID: {nueva_empresa.Id}")
    
    # 2. Verificar Log de Creación
    log_crear = AuditoriaLog.query.filter_by(
        TablaAfectada='Empresas', 
        RegistroId=nueva_empresa.Id, 
        Accion='CREAR'
    ).first()
    
    if log_crear:
        print("✅ Log de CREACIÓN encontrado.")
        print(f"   Detalle: {log_crear.DetalleCambio}")
    else:
        print("❌ Log de CREACIÓN NO encontrado.")

    # Limpieza
    # db.session.delete(nueva_empresa)
    # db.session.commit()
