from app import create_app
from app.services.auth_service import AuthService
from app.models.auth_models import Persona
from app.extensions import db

app = create_app()

with app.app_context():
    try:
        # Verificar si ya existe
        if Persona.query.filter_by(Correo='admin@siicsa.com').first():
            print("El usuario admin ya existe.")
        else:
            print("Creando usuario admin...")
            AuthService.create_user({
                'nombre': 'Administrador',
                'apellido': 'Sistema',
                'correo': 'admin@siicsa.com',
                'password': 'AdminPassword123!'
            })
            print("Usuario creado exitosamente.")
            
        # Verificar celular
        user = Persona.query.filter_by(Correo='admin@siicsa.com').first()
        if user and not user.Celular:
            user.Celular = '573001234567'
            db.session.commit()
            print("Celular actualizado.")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Error al crear usuario: {e}")
        db.session.rollback()
