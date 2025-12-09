from app import create_app
from app.models.auth_models import Persona
from app.extensions import db
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    try:
        user = Persona.query.filter_by(Correo='admin@siicsa.com').first()
        if user:
            print(f"Found user: {user.Nombre} {user.Apellido}")
            user.PasswordHash = generate_password_hash('AdminPassword123!')
            user.Activo = True
            user.IntentosFallidos = 0
            user.BloqueoHasta = None
            db.session.commit()
            print("Password reset successfully.")
        else:
            print("User admin@siicsa.com not found. Creating...")
            hashed = generate_password_hash('AdminPassword123!')
            new_user = Persona(
                Nombre='Administrador',
                Apellido='Sistema',
                Correo='admin@siicsa.com',
                PasswordHash=hashed,
                EsUsuarioSistema=True,
                Activo=True
            )
            db.session.add(new_user)
            db.session.commit()
            print("User created.")
            
    except Exception as e:
        print(f"Error: {e}")
