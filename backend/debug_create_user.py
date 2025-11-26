from app import create_app
from app.services.config_service import ConfigService
from app.models.auth_models import Permiso, Rol
import traceback

app = create_app()

with app.app_context():
    try:
        print("Buscando permiso...")
        permiso = Permiso.query.first()
        if not permiso:
            print("No hay permisos")
            exit()
            
        print(f"Permiso: {permiso.Id}")
        
        data = {
            'Nombre': 'Debug',
            'Apellido': 'User',
            'Correo': 'debug@test.com',
            'Password': 'User123!',
            'EsUsuarioSistema': True,
            'RolId': Rol.query.first().Id,
            'PermisosEspecificos': [permiso.Id]
        }
        
        print("Intentando crear usuario...")
        ConfigService.create_user(data)
        print("Usuario creado OK")
        
    except Exception:
        with open('error.log', 'w', encoding='utf-8') as f:
            traceback.print_exc(file=f)
