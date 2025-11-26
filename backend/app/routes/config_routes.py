from flask import Blueprint, request, jsonify
from app.services.config_service import ConfigService
from app.utils.decorators import token_required, requires_permission

config_bp = Blueprint('config', __name__, url_prefix='/api/config')

# --- GEOGRAFÍA ---
@config_bp.route('/departments', methods=['GET'])
@token_required
def get_departments(current_user):
    from app.models.core_models import Departamento
    try:
        depts = Departamento.query.order_by(Departamento.Nombre).all()
        return jsonify([{'Id': d.Id, 'Nombre': d.Nombre} for d in depts])
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@config_bp.route('/cities/<int:dept_id>', methods=['GET'])
@token_required
def get_cities(current_user, dept_id):
    from app.models.core_models import Ciudad
    try:
        cities = Ciudad.query.filter_by(DepartamentoId=dept_id).order_by(Ciudad.Nombre).all()
        return jsonify([{'Id': c.Id, 'Nombre': c.Nombre} for c in cities])
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# --- EMPRESAS ---
@config_bp.route('/companies', methods=['GET'])
@token_required
def get_companies(current_user):
    # TODO: Filtrar si es Tenant
    companies = ConfigService.get_all_companies()
    return jsonify([{
        'Id': c.Id, 'NIT': c.NIT, 'RazonSocial': c.RazonSocial, 'Direccion': c.Direccion, 'Telefono': c.Telefono,
        'EsCliente': c.EsCliente, 'Activo': c.Activo, 'CiudadId': c.CiudadId
    } for c in companies]), 200

@config_bp.route('/companies', methods=['POST'])
@token_required
@requires_permission('sys_company:manage')
def create_company(current_user):
    data = request.get_json()
    try:
        new_company = ConfigService.create_company(data)
        return jsonify({'message': 'Empresa creada', 'Id': new_company.Id}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@config_bp.route('/companies/<int:company_id>', methods=['PUT', 'POST']) # POST para compatibilidad si axios falla con PUT
@token_required
@requires_permission('sys_company:manage')
def update_company(current_user, company_id):
    data = request.get_json()
    try:
        updated = ConfigService.update_company(company_id, data)
        if not updated:
            return jsonify({'message': 'Empresa no encontrada'}), 404
        return jsonify({'message': 'Empresa actualizada'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# --- SEDES ---
@config_bp.route('/sedes', methods=['GET'])
@token_required
def get_sedes(current_user):
    empresa_id = request.args.get('EmpresaId')
    filters = {}
    if empresa_id:
        filters['EmpresaId'] = empresa_id
        
    sedes = ConfigService.get_sedes(filters)
    return jsonify([{
        'Id': s.Id, 'NombreSede': s.NombreSede, 'EmpresaId': s.EmpresaId,
        'Direccion': s.Direccion, 'Telefono': s.Telefono, 'Activo': s.Activo, 'CiudadId': s.CiudadId
    } for s in sedes]), 200

@config_bp.route('/sedes', methods=['POST'])
@token_required
@requires_permission('sys_company:manage')
def create_sede(current_user):
    data = request.get_json()
    try:
        new_sede = ConfigService.create_sede(data)
        return jsonify({'message': 'Sede creada', 'Id': new_sede.Id}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@config_bp.route('/sedes/<int:sede_id>', methods=['PUT', 'POST'])
@token_required
@requires_permission('sys_company:manage')
def update_sede(current_user, sede_id):
    data = request.get_json()
    try:
        updated = ConfigService.update_sede(sede_id, data)
        if not updated:
            return jsonify({'message': 'Sede no encontrada'}), 404
        return jsonify({'message': 'Sede actualizada'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# --- ROLES ---
@config_bp.route('/roles', methods=['GET'])
@token_required
def get_roles(current_user):
    try:
        roles = ConfigService.get_all_roles()
        return jsonify([{'Id': r.Id, 'Nombre': r.Nombre, 'Descripcion': r.Descripcion} for r in roles]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# --- PERMISOS ---
@config_bp.route('/permissions', methods=['GET'])
@token_required
def get_permissions(current_user):
    try:
        perms = ConfigService.get_all_permissions()
        return jsonify([{
            'Id': p.Id, 
            'Codigo': p.Codigo, 
            'Descripcion': p.Descripcion,
            'Modulo': p.Modulo
        } for p in perms]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# --- USUARIOS ---
@config_bp.route('/users', methods=['GET'])
@token_required
@requires_permission('sys_users:view_all')
def get_users(current_user):
    users = ConfigService.get_users({'EsUsuarioSistema': True})
    return jsonify([{
        'Id': u.Id, 'Nombre': u.Nombre, 'Apellido': u.Apellido, 
        'Correo': u.Correo, 'Rol': u.Rol.Nombre if u.Rol else 'Sin Rol',
        'Activo': u.Activo, 'CargoId': u.CargoId, 'AreaId': u.AreaId, 'SedeId': u.SedeId, 'RolId': u.RolId,
        'PermisosEspecificos': [p.Id for p in u.PermisosEspecificos]
    } for u in users]), 200

@config_bp.route('/users', methods=['POST'])
@token_required
@requires_permission('sys_users:manage_all')
def create_user(current_user):
    data = request.get_json()
    try:
        new_user = ConfigService.create_user(data)
        return jsonify({'message': 'Usuario creado', 'Id': new_user.Id}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': 'Error interno'}), 500

@config_bp.route('/users/<int:user_id>', methods=['PUT', 'POST'])
@token_required
@requires_permission('sys_users:manage_all')
def update_user(current_user, user_id):
    data = request.get_json()
    try:
        updated = ConfigService.update_user(user_id, data)
        if not updated:
            return jsonify({'message': 'Usuario no encontrado'}), 404
        return jsonify({'message': 'Usuario actualizado'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# --- CATÁLOGOS ---
@config_bp.route('/catalogs/<catalog_name>', methods=['GET'])
@token_required
def get_catalog(current_user, catalog_name):
    try:
        items = ConfigService.get_catalog_items(catalog_name)
        # Serialización genérica (asume Id y Nombre/Capacidad/Velocidad)
        result = []
        for item in items:
            data = {'Id': item.Id}
            if hasattr(item, 'Nombre'): data['Nombre'] = item.Nombre
            if hasattr(item, 'Capacidad'): data['Capacidad'] = item.Capacidad
            if hasattr(item, 'Velocidad'): data['Velocidad'] = item.Velocidad
            if hasattr(item, 'Activo'): data['Activo'] = item.Activo
            result.append(data)
        return jsonify(result), 200
    except ValueError:
        return jsonify({'message': 'Catálogo no encontrado'}), 404

@config_bp.route('/catalogs/<catalog_name>', methods=['POST'])
@token_required
@requires_permission('catalogs:create')
def create_catalog_item(current_user, catalog_name):
    data = request.get_json()
    try:
        new_item = ConfigService.create_catalog_item(catalog_name, data)
        return jsonify({'message': 'Item creado', 'Id': new_item.Id}), 201
    except ValueError:
        return jsonify({'message': 'Catálogo no encontrado'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 400
