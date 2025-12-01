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
    # Enrich with City name (this could be optimized with a join in the service/query)
    from app.models.core_models import Ciudad
    result = []
    for s in sedes:
        ciudad_nombre = ''
        if s.CiudadId:
            ciudad = Ciudad.query.get(s.CiudadId)
            if ciudad:
                ciudad_nombre = ciudad.Nombre
        
        result.append({
            'Id': s.Id, 'NombreSede': s.NombreSede, 'EmpresaId': s.EmpresaId,
            'Direccion': s.Direccion, 'Telefono': s.Telefono, 'Activo': s.Activo, 
            'CiudadId': s.CiudadId, 'Ciudad': ciudad_nombre
        })
    return jsonify(result), 200

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
        return jsonify([{
            'Id': r.Id, 
            'Nombre': r.Nombre, 
            'Descripcion': r.Descripcion,
            'Permisos': [p.Id for p in r.Permisos]
        } for r in roles]), 200
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
        'Correo': u.Correo, 'Celular': u.Celular, 'Rol': u.Rol.Nombre if u.Rol else 'Sin Rol',
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
        # Convertir request.args a dict para filtrar
        filters = request.args.to_dict()
        items = ConfigService.get_catalog_items(catalog_name, filters)
        # Serialización genérica (asume Id y Nombre/Capacidad/Velocidad)
        result = []
        for item in items:
            data = {'Id': item.Id}
            if hasattr(item, 'Nombre'): data['Nombre'] = item.Nombre
            if hasattr(item, 'Capacidad'): data['Capacidad'] = item.Capacidad
            if hasattr(item, 'Velocidad'): data['Velocidad'] = item.Velocidad
            if hasattr(item, 'Activo'): data['Activo'] = item.Activo
            # Incluir FKs para jerarquías
            if hasattr(item, 'MarcaId'): data['MarcaId'] = item.MarcaId
            if hasattr(item, 'TipoId'): data['TipoId'] = item.TipoId
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

@config_bp.route('/catalogs/<catalog_name>/<int:item_id>', methods=['PUT', 'POST'])
@token_required
@requires_permission('catalogs:create') # Usamos el mismo permiso de crear por ahora, o podríamos crear 'catalogs:manage'
def update_catalog_item(current_user, catalog_name, item_id):
    data = request.get_json()
    try:
        updated = ConfigService.update_catalog_item(catalog_name, item_id, data)
        if not updated:
            return jsonify({'message': 'Item no encontrado'}), 404
        return jsonify({'message': 'Item actualizado'}), 200
    except ValueError:
        return jsonify({'message': 'Catálogo no válido'}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# --- CONFIGURACIÓN DE RAM ---
@config_bp.route('/tipos_ram', methods=['GET'])
@token_required
@requires_permission('catalogs:view')
def get_tipos_ram(current_user):
    from app.models.inventory_models import TipoRAM
    try:
        items = TipoRAM.query.filter_by(Activo=True).order_by(TipoRAM.Nombre).all()
        return jsonify([{'Id': i.Id, 'Nombre': i.Nombre} for i in items])
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@config_bp.route('/tipos_ram', methods=['POST'])
@token_required
@requires_permission('catalogs:create')
def create_tipo_ram(current_user):
    from app.models.inventory_models import TipoRAM
    from app.extensions import db
    data = request.get_json()
    try:
        new_item = TipoRAM(Nombre=data['Nombre'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Tipo RAM creado', 'Id': new_item.Id}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@config_bp.route('/capacidades_ram', methods=['GET'])
@token_required
@requires_permission('catalogs:view')
def get_capacidades_ram(current_user):
    from app.models.inventory_models import CapacidadRAM
    try:
        # Ordenar alfanuméricamente podría requerir lógica extra, por ahora alfabético
        items = CapacidadRAM.query.filter_by(Activo=True).order_by(CapacidadRAM.Capacidad).all()
        return jsonify([{'Id': i.Id, 'Nombre': i.Capacidad} for i in items])
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@config_bp.route('/capacidades_ram', methods=['POST'])
@token_required
@requires_permission('catalogs:create')
def create_capacidad_ram(current_user):
    from app.models.inventory_models import CapacidadRAM
    from app.extensions import db
    data = request.get_json()
    try:
        # Frontend envía 'Nombre', backend espera 'Capacidad'
        new_item = CapacidadRAM(Capacidad=data['Nombre']) 
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Capacidad RAM creada', 'Id': new_item.Id}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@config_bp.route('/velocidades_ram', methods=['GET'])
@token_required
@requires_permission('catalogs:view')
def get_velocidades_ram(current_user):
    from app.models.inventory_models import BusRAM
    try:
        query = BusRAM.query.filter_by(Activo=True)
        if 'TipoRAMId' in request.args:
            query = query.filter_by(TipoId=request.args['TipoRAMId'])
        
        items = query.order_by(BusRAM.Velocidad).all()
        return jsonify([{'Id': i.Id, 'Nombre': i.Velocidad, 'TipoRAMId': i.TipoId, 'Activo': i.Activo} for i in items])
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@config_bp.route('/velocidades_ram', methods=['POST'])
@token_required
@requires_permission('catalogs:create')
def create_velocidad_ram(current_user):
    from app.models.inventory_models import BusRAM
    from app.extensions import db
    data = request.get_json()
    try:
        # Frontend envía 'Nombre' y 'TipoRAMId', backend espera 'Velocidad' y 'TipoId'
        new_item = BusRAM(Velocidad=data['Nombre'], TipoId=data['TipoRAMId'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Velocidad RAM creada', 'Id': new_item.Id}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@config_bp.route('/velocidades_ram/<int:id>', methods=['PUT'])
@token_required
@requires_permission('catalogs:create') # Reutilizamos permiso de crear por ahora
def update_velocidad_ram(current_user, id):
    from app.models.inventory_models import BusRAM
    from app.extensions import db
    data = request.get_json()
    try:
        item = BusRAM.query.get_or_404(id)
        if 'Nombre' in data:
            item.Velocidad = data['Nombre']
        if 'Activo' in data:
            item.Activo = data['Activo']
            
        db.session.commit()
        return jsonify({'message': 'Velocidad actualizada'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400
        return jsonify({'message': 'Velocidad actualizada'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# --- ALMACENAMIENTO ---

@config_bp.route('/tipos_almacenamiento', methods=['GET', 'POST'])
@token_required
def tipos_almacenamiento(current_user):
    from app.models.inventory_models import TipoAlmacenamiento
    from app.extensions import db
    
    if request.method == 'GET':
        # Verificar permiso de lectura manualmente o separar endpoints
        if not current_user.has_permission('catalogs:view'):
            return jsonify({'message': 'Acceso denegado'}), 403
        items = TipoAlmacenamiento.query.all()
        return jsonify([{'Id': i.Id, 'Nombre': i.Nombre, 'Activo': i.Activo} for i in items])
    
    if request.method == 'POST':
        if not current_user.has_permission('catalogs:create'):
            return jsonify({'message': 'Acceso denegado'}), 403
        data = request.get_json()
        if not data or 'Nombre' not in data:
            return jsonify({'message': 'Faltan datos'}), 400
        
        # Find or Create
        existing = TipoAlmacenamiento.query.filter_by(Nombre=data['Nombre']).first()
        if existing:
            return jsonify({'message': 'Ya existe', 'Id': existing.Id}), 200
            
        new_item = TipoAlmacenamiento(Nombre=data['Nombre'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Creado', 'Id': new_item.Id}), 201

@config_bp.route('/capacidades_almacenamiento', methods=['GET', 'POST'])
@token_required
def capacidades_almacenamiento(current_user):
    from app.models.inventory_models import CapacidadAlmacenamiento
    from app.extensions import db
    
    if request.method == 'GET':
        if not current_user.has_permission('catalogs:view'):
            return jsonify({'message': 'Acceso denegado'}), 403
        items = CapacidadAlmacenamiento.query.all()
        return jsonify([{'Id': i.Id, 'Nombre': i.Capacidad, 'Activo': i.Activo} for i in items])
    
    if request.method == 'POST':
        if not current_user.has_permission('catalogs:create'):
            return jsonify({'message': 'Acceso denegado'}), 403
        data = request.get_json()
        if not data or 'Nombre' not in data:
            return jsonify({'message': 'Faltan datos'}), 400
            
        existing = CapacidadAlmacenamiento.query.filter_by(Capacidad=data['Nombre']).first()
        if existing:
            return jsonify({'message': 'Ya existe', 'Id': existing.Id}), 200
            
        new_item = CapacidadAlmacenamiento(Capacidad=data['Nombre'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Creado', 'Id': new_item.Id}), 201

@config_bp.route('/protocolos_almacenamiento', methods=['GET', 'POST'])
@token_required
def protocolos_almacenamiento(current_user):
    from app.models.inventory_models import ProtocoloAlmacenamiento
    from app.extensions import db
    
    if request.method == 'GET':
        if not current_user.has_permission('catalogs:view'):
            return jsonify({'message': 'Acceso denegado'}), 403
        query = ProtocoloAlmacenamiento.query
        if 'TipoId' in request.args:
            query = query.filter_by(TipoId=request.args['TipoId'])
        items = query.all()
        return jsonify([{'Id': i.Id, 'Nombre': i.Nombre, 'TipoId': i.TipoId, 'Activo': i.Activo} for i in items])
    
    if request.method == 'POST':
        if not current_user.has_permission('catalogs:create'):
            return jsonify({'message': 'Acceso denegado'}), 403
        data = request.get_json()
        new_item = ProtocoloAlmacenamiento(Nombre=data['Nombre'], TipoId=data['TipoId'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Creado', 'Id': new_item.Id}), 201

@config_bp.route('/protocolos_almacenamiento/<int:id>', methods=['PUT'])
@token_required
@requires_permission('catalogs:create')
def update_protocolo_almacenamiento(current_user, id):
    from app.models.inventory_models import ProtocoloAlmacenamiento
    from app.extensions import db
    data = request.get_json()
    item = ProtocoloAlmacenamiento.query.get_or_404(id)
    if 'Nombre' in data: item.Nombre = data['Nombre']
    if 'Activo' in data: item.Activo = data['Activo']
    db.session.commit()
    return jsonify({'message': 'Actualizado'}), 200

@config_bp.route('/factores_forma_almacenamiento', methods=['GET', 'POST'])
@token_required
def factores_forma_almacenamiento(current_user):
    from app.models.inventory_models import FactorFormaAlmacenamiento
    from app.extensions import db
    
    if request.method == 'GET':
        if not current_user.has_permission('catalogs:view'):
            return jsonify({'message': 'Acceso denegado'}), 403
        query = FactorFormaAlmacenamiento.query
        if 'TipoId' in request.args:
            query = query.filter_by(TipoId=request.args['TipoId'])
        items = query.all()
        return jsonify([{'Id': i.Id, 'Nombre': i.Nombre, 'TipoId': i.TipoId, 'Activo': i.Activo} for i in items])
    
    if request.method == 'POST':
        if not current_user.has_permission('catalogs:create'):
            return jsonify({'message': 'Acceso denegado'}), 403
        data = request.get_json()
        new_item = FactorFormaAlmacenamiento(Nombre=data['Nombre'], TipoId=data['TipoId'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Creado', 'Id': new_item.Id}), 201

@config_bp.route('/factores_forma_almacenamiento/<int:id>', methods=['PUT'])
@token_required
@requires_permission('catalogs:create')
def update_factor_forma_almacenamiento(current_user, id):
    from app.models.inventory_models import FactorFormaAlmacenamiento
    from app.extensions import db
    data = request.get_json()
    item = FactorFormaAlmacenamiento.query.get_or_404(id)
    if 'Nombre' in data: item.Nombre = data['Nombre']
    if 'Activo' in data: item.Activo = data['Activo']
    db.session.commit()
    return jsonify({'message': 'Actualizado'}), 200
