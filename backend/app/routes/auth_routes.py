from flask import Blueprint, request, jsonify, make_response
from app.services.auth_service import AuthService
from app.models.auth_models import Persona
from app.extensions import db
import jwt
import os
from functools import wraps

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

# Decorador para verificar token (opcional si usamos cookies, pero útil para proteger rutas)
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('auth_token')
        if not token:
            return jsonify({'message': 'Token faltante'}), 401
        try:
            data = jwt.decode(token, os.getenv('SECRET_KEY', 'dev_key'), algorithms=['HS256'])
            current_user = Persona.query.get(data['sub'])
        except:
            return jsonify({'message': 'Token inválido'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('identifier') or not data.get('password'):
        return jsonify({'message': 'Faltan credenciales'}), 400

    result = AuthService.login_user(data['identifier'], data['password'])

    if not result['success']:
        return jsonify({'message': result['message']}), 401

    if result.get('requires_2fa'):
        return jsonify({
            'message': '2FA Requerido',
            'requires_2fa': True,
            'temp_token': result['temp_token'] # El frontend debe enviar esto en el paso 2
        }), 200

    # Login exitoso completo
    rol_perms = set(p.Codigo for p in result['user'].Rol.Permisos) if result['user'].Rol else set()
    user_perms = set(p.Codigo for p in result['user'].PermisosEspecificos)
    all_perms = list(rol_perms.union(user_perms))
    
    response = make_response(jsonify({
        'message': 'Login exitoso',
        'token': result['token'], # Add token here for frontend usage
        'user': {
            'Nombre': result['user'].Nombre,
            'Apellido': result['user'].Apellido,
            'Cargo': result['user'].Cargo.Nombre if result['user'].Cargo else 'Sin Cargo',
            'Rol': result['user'].Rol.Nombre if result['user'].Rol else 'Sin Rol',
            'Scope': result['user'].Rol.Scope if result['user'].Rol else 'NONE',
            'Permisos': all_perms
        }
    }))
    
    # Set Cookie HttpOnly
    response.set_cookie(
        'auth_token',
        result['token'],
        httponly=True,
        secure=False, # True en producción con HTTPS
        samesite='Lax',
        max_age=7*24*3600 # 7 días
    )
    
    return response

@auth_bp.route('/verify-2fa', methods=['POST'])
def verify_2fa():
    data = request.get_json()
    temp_token = data.get('temp_token')
    code = data.get('code')
    
    if not temp_token or not code:
        return jsonify({'message': 'Faltan datos'}), 400
        
    try:
        # Decodificar token temporal para obtener user_id
        payload = jwt.decode(temp_token, os.getenv('SECRET_KEY', 'dev_key'), algorithms=['HS256'])
        if payload.get('type') != 'temp':
            return jsonify({'message': 'Token inválido'}), 401
            
        user_id = payload['sub']
        
        if AuthService.verify_2fa(user_id, code):
            # 2FA Correcto -> Generar token final
            final_token = AuthService.generate_token(user_id)
            user = Persona.query.get(user_id)
            
            response = make_response(jsonify({
                'message': '2FA Verificado',
                'user': {
                    'Nombre': user.Nombre,
                    'Apellido': user.Apellido,
                    'Cargo': user.Cargo.Nombre if user.Cargo else 'Sin Cargo'
                }
            }))
            
            response.set_cookie(
                'auth_token',
                final_token,
                httponly=True,
                secure=False,
                samesite='Strict',
                max_age=8*3600
            )
            return response
        else:
            return jsonify({'message': 'Código incorrecto'}), 401
            
    except Exception as e:
        return jsonify({'message': 'Token expirado o inválido'}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    # Auditoría de Logout
    try:
        token = request.cookies.get('auth_token')
        if token:
            payload = jwt.decode(token, os.getenv('SECRET_KEY', 'dev_key'), algorithms=['HS256'])
            user_id = payload.get('sub')
            
            if user_id:
                from app.models.audit_models import AuditoriaLog
                from sqlalchemy import insert
                from datetime import datetime
                
                stmt = insert(AuditoriaLog).values(
                    TablaAfectada='Personas',
                    RegistroId=user_id,
                    Accion='LOGOUT',
                    UsuarioId=user_id,
                    Fecha=datetime.now(),
                    DetalleCambio="Cierre de Sesión",
                    ValorDespues="Logout"
                )
                db.session.execute(stmt)
                db.session.commit()
    except Exception as e:
        print(f"Error auditable logout: {e}")

    response = make_response(jsonify({'message': 'Sesión cerrada'}))
    response.set_cookie('auth_token', '', expires=0)
    return response

@auth_bp.route('/me', methods=['GET'])
@token_required
def get_current_user(current_user):
    rol_perms = set(p.Codigo for p in current_user.Rol.Permisos) if current_user.Rol else set()
    user_perms = set(p.Codigo for p in current_user.PermisosEspecificos)
    all_perms = list(rol_perms.union(user_perms))

    return jsonify({
        'Nombre': current_user.Nombre,
        'Apellido': current_user.Apellido,
        'Correo': current_user.Correo,
        'Cargo': current_user.Cargo.Nombre if current_user.Cargo else 'Sin Cargo',
        'Rol': current_user.Rol.Nombre if current_user.Rol else 'Sin Rol',
        'Scope': current_user.Rol.Scope if current_user.Rol else 'NONE',
        'Permisos': all_perms
    })
