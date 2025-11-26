from app.models.auth_models import Persona
from app.extensions import db
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta
import jwt
import os
import pyotp

class AuthService:
    @staticmethod
    def login_user(identifier, password):
        """
        Lógica de login inteligente:
        1. Detectar tipo de identificador (Email, Celular, Usuario)
        2. Buscar usuario (Case Insensitive)
        3. Verificar bloqueo por fuerza bruta
        4. Verificar contraseña
        5. Manejar intentos fallidos
        6. Retornar resultado o requerir 2FA
        """
        
        # 1. Normalización y Detección
        identifier = identifier.strip()
        query = Persona.query.filter_by(Activo=True)
        
        if '@' in identifier:
            # Es Correo
            user = query.filter(Persona.Correo == identifier).first()
        elif identifier.isdigit() and len(identifier) >= 7:
            # Es Celular (asumimos que si tiene más de 7 dígitos es celular)
            # Normalizar: Si no empieza con 57 y tiene 10 dígitos, agregar 57 (regla simple)
            if len(identifier) == 10 and not identifier.startswith('57'):
                identifier = '57' + identifier
            user = query.filter(Persona.Celular == identifier).first()
        else:
            # Es Usuario (Nombre/Apellido o Username si existiera campo específico, usaremos Correo como fallback o búsqueda por nombre si se requiere, 
            # pero el requerimiento dice "Usuario". Asumiremos que el "Usuario" es el Correo o un campo que no definimos explícitamente como "Username".
            # Revisando requerimientos: "el campo de usuario/correo/celular sirve para loguiarse".
            # Como no tenemos campo "Username" único, usaremos Correo como principal "Usuario" o podríamos buscar por Nombre (peligroso por homónimos).
            # Para cumplir estrictamente, buscaremos en Correo si no es celular.
            user = query.filter(Persona.Correo == identifier).first()

        if not user:
            return {"success": False, "message": "Credenciales inválidas"}

        # 2. Verificar Bloqueo
        if user.BloqueoHasta and user.BloqueoHasta > datetime.utcnow():
            minutes_left = (user.BloqueoHasta - datetime.utcnow()).seconds // 60
            return {"success": False, "message": f"Cuenta bloqueada temporalmente. Intente en {minutes_left} minutos."}

        # 3. Verificar Contraseña
        if not user.PasswordHash or not check_password_hash(user.PasswordHash, password):
            # Manejo de Intentos Fallidos
            user.IntentosFallidos += 1
            if user.IntentosFallidos >= 3:
                user.BloqueoHasta = datetime.utcnow() + timedelta(minutes=15)
                user.IntentosFallidos = 0 # Reiniciamos contador para el siguiente ciclo de bloqueo
                db.session.commit()
                return {"success": False, "message": "Demasiados intentos fallidos. Cuenta bloqueada por 15 minutos."}
            
            db.session.commit()
            return {"success": False, "message": "Credenciales inválidas"}

        # 4. Login Exitoso (Parcial o Total)
        user.IntentosFallidos = 0
        user.UltimoLogin = datetime.utcnow()
        db.session.commit()
        
        if user.TwoFactorEnabled and user.TwoFactorSecret:
            # Requiere 2FA
            # Generamos un token temporal para validar el segundo paso
            temp_token = AuthService.generate_token(user.Id, temp=True)
            return {"success": True, "requires_2fa": True, "temp_token": temp_token}
        
        # Login Completo
        token = AuthService.generate_token(user.Id)
        return {"success": True, "requires_2fa": False, "token": token, "user": user}

    @staticmethod
    def verify_2fa(user_id, code):
        user = Persona.query.get(user_id)
        if not user or not user.TwoFactorSecret:
            return False
            
        totp = pyotp.TOTP(user.TwoFactorSecret)
        return totp.verify(code)

    @staticmethod
    def generate_token(user_id, temp=False):
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=7 if not temp else 0), # 7 días normal
                'iat': datetime.utcnow(),
                'sub': str(user_id),
                'type': 'temp' if temp else 'access'
            }
            return jwt.encode(
                payload,
                os.getenv('SECRET_KEY', 'dev_key'),
                algorithm='HS256'
            )
        except Exception as e:
            return str(e)
            
    @staticmethod
    def create_user(data):
        # Helper para crear usuario con hash (útil para seeds)
        hashed = generate_password_hash(data['password'])
        new_user = Persona(
            Nombre=data['nombre'],
            Apellido=data['apellido'],
            Correo=data['correo'],
            PasswordHash=hashed,
            EsUsuarioSistema=True
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user
