from app import create_app, db
from app.services.auth_service import AuthService
from app.models.auth_models import Persona
from werkzeug.security import generate_password_hash
from flask import g

app = create_app()

# Simular contexto de request
with app.test_request_context('/api/auth/login', method='POST'):
    with app.app_context():
        try:
            print("--- Debug Login (Request Context) ---")
            # 1. Asegurar usuario de prueba
            email = 'debug_admin@siicsa.com'
            password = 'password123'
            
            user = Persona.query.filter_by(Correo=email).first()
            if not user:
                print("Creando usuario de prueba...")
                user = Persona(
                    Nombre='Debug',
                    Apellido='Admin',
                    Correo=email,
                    PasswordHash=generate_password_hash(password),
                    EsUsuarioSistema=True
                )
                db.session.add(user)
                db.session.commit()
            else:
                user.IntentosFallidos = 0
                user.BloqueoHasta = None
                db.session.commit()
                
            print(f"Usuario {email} listo.")

            # 2. Intentar Login
            print("Llamando AuthService.login_user...")
            result = AuthService.login_user(email, password)
            print(f"Resultado Login: {result}")

        except Exception as e:
            print("\n!!! EXCEPCIÓN CAPTURADA !!!")
            import traceback
            traceback.print_exc()
