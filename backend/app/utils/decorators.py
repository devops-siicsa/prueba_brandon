from functools import wraps
from flask import request, jsonify
from app.models.auth_models import Persona
import jwt
import os

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('auth_token')
        if not token:
            return jsonify({'message': 'Token faltante'}), 401
        try:
            data = jwt.decode(token, os.getenv('SECRET_KEY', 'dev_key'), algorithms=['HS256'])
            current_user = Persona.query.get(data['sub'])
            if not current_user:
                return jsonify({'message': 'Usuario inválido'}), 401
        except Exception as e:
            print(f"Error decodificando token: {str(e)}")
            return jsonify({'message': 'Token inválido'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

def requires_permission(permission_code):
    def decorator(f):
        @wraps(f)
        def decorated_function(current_user, *args, **kwargs):
            # Verificar si el usuario tiene rol y si ese rol tiene el permiso
            if not current_user.Rol:
                return jsonify({'message': 'Acceso denegado: Sin rol asignado'}), 403
            
            # Super Admin suele tener todo, pero validemos explícitamente
            permisos_usuario = [p.Codigo for p in current_user.Rol.Permisos]
            
            if permission_code not in permisos_usuario:
                 return jsonify({'message': f'Acceso denegado: Requiere permiso {permission_code}'}), 403
                 
            return f(current_user, *args, **kwargs)
        return decorated_function
    return decorator
