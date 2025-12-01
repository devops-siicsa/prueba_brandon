from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.inventory_models import Equipo
from app.utils.decorators import token_required, requires_permission
from datetime import datetime

inventory_bp = Blueprint('inventory', __name__, url_prefix='/api/inventory')

# --- EQUIPOS ---

@inventory_bp.route('/equipos', methods=['GET'])
@token_required
def get_equipos(current_user):
    try:
        # Filtros básicos
        empresa_id = request.args.get('EmpresaId')
        sede_id = request.args.get('SedeId')
        
        query = Equipo.query
        
        if empresa_id:
            query = query.filter_by(EmpresaId=empresa_id)
        # TODO: Agregar más filtros según necesidad (Serial, Codigo, etc.)
            
        equipos = query.order_by(Equipo.FechaCreacion.desc()).all()
        
        return jsonify([{
            'Id': e.Id,
            'CodigoEquipo': e.CodigoEquipo,
            'EmpresaId': e.EmpresaId,
            'UsuarioAsignadoId': e.UsuarioAsignadoId,
            'EstadoEquipoId': e.EstadoEquipoId,
            'TipoEquipoId': e.TipoEquipoId,
            'FabricanteId': e.FabricanteId,
            'Modelo': e.Modelo,
            'Serial': e.Serial,
            'FechaCreacion': e.FechaCreacion.isoformat() if e.FechaCreacion else None
        } for e in equipos]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@inventory_bp.route('/equipos/<int:equipo_id>', methods=['GET'])
@token_required
def get_equipo_detail(current_user, equipo_id):
    try:
        equipo = Equipo.query.get_or_404(equipo_id)
        
        # Cargar relaciones
        from app.models.inventory_models import EquipoProcesador, EquipoRAM, EquipoAlmacenamiento
        
        procesadores = EquipoProcesador.query.filter_by(EquipoId=equipo.Id).all()
        memorias = EquipoRAM.query.filter_by(EquipoId=equipo.Id).all()
        discos = EquipoAlmacenamiento.query.filter_by(EquipoId=equipo.Id).all()
        
        return jsonify({
            'Id': equipo.Id,
            'CodigoEquipo': equipo.CodigoEquipo,
            'EmpresaId': equipo.EmpresaId,
            'UsuarioAsignadoId': equipo.UsuarioAsignadoId,
            'UsuarioNombre': equipo.UsuarioAsignado.NombreCompleto if equipo.UsuarioAsignadoId and hasattr(equipo, 'UsuarioAsignado') else None, # Asumiendo relación
            'EstadoEquipoId': equipo.EstadoEquipoId,
            'TipoEquipoId': equipo.TipoEquipoId,
            'FabricanteId': equipo.FabricanteId,
            'Modelo': equipo.Modelo,
            'Serial': equipo.Serial,
            'FotoSerialUrl': equipo.FotoSerialUrl,
            'EsPropio': equipo.EsPropio,
            'ProveedorAlquiler': equipo.ProveedorAlquiler,
            'CodigoAlquiler': equipo.CodigoAlquiler,
            'SistemaOperativoId': equipo.SistemaOperativoId,
            'LicenciaSO': equipo.LicenciaSO,
            'OfimaticaId': equipo.OfimaticaId,
            'NombreOfimatica': equipo.NombreOfimatica,
            'LicenciaOfimatica': equipo.LicenciaOfimatica,
            'AntivirusId': equipo.AntivirusId,
            'EquipoPertenece': equipo.EquipoPertenece,
            'NombreEnRed': equipo.NombreEnRed,
            'UltimoMantenimiento': equipo.UltimoMantenimiento.isoformat() if equipo.UltimoMantenimiento else None,
            'FechaCreacion': equipo.FechaCreacion.isoformat() if equipo.FechaCreacion else None,
            'CreadoPorId': equipo.CreadoPorId,
            
            # Detalles Hardware
            'Procesadores': [{'Id': p.Id, 'GeneracionId': p.GeneracionId} for p in procesadores],
            'MemoriasRAM': [{'Id': m.Id, 'CapacidadId': m.CapacidadId, 'BusId': m.BusId, 'SlotNumero': m.SlotNumero} for m in memorias],
            'Almacenamiento': [{'Id': d.Id, 'ProtocoloId': d.ProtocoloId, 'FactorFormaId': d.FactorFormaId, 'CapacidadId': d.CapacidadId, 'SlotNumero': d.SlotNumero} for d in discos]
        }), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@inventory_bp.route('/equipos', methods=['POST'])
@token_required
@requires_permission('inventory:create')
def create_equipo(current_user):
    data = request.get_json()
    try:
        # Validaciones básicas
        if not data.get('CodigoEquipo'):
            return jsonify({'message': 'El código del equipo es obligatorio'}), 400
            
        # Verificar duplicados
        if Equipo.query.filter_by(CodigoEquipo=data['CodigoEquipo']).first():
            return jsonify({'message': 'El código de equipo ya existe'}), 400

        new_equipo = Equipo(
            CodigoEquipo=data['CodigoEquipo'],
            EmpresaId=data.get('EmpresaId'),
            UsuarioAsignadoId=data.get('UsuarioAsignadoId'),
            EstadoEquipoId=data.get('EstadoEquipoId'),
            TipoEquipoId=data.get('TipoEquipoId'),
            FabricanteId=data.get('FabricanteId'),
            Modelo=data.get('Modelo'),
            Serial=data.get('Serial'),
            EsPropio=data.get('EsPropio', True),
            ProveedorAlquiler=data.get('ProveedorAlquiler'),
            CodigoAlquiler=data.get('CodigoAlquiler'),
            SistemaOperativoId=data.get('SistemaOperativoId'),
            LicenciaSO=data.get('LicenciaSO'),
            OfimaticaId=data.get('OfimaticaId'),
            NombreOfimatica=data.get('NombreOfimatica'),
            LicenciaOfimatica=data.get('LicenciaOfimatica'),
            AntivirusId=data.get('AntivirusId'),
            EquipoPertenece=data.get('EquipoPertenece'),
            NombreEnRed=data.get('NombreEnRed'),
            CreadoPorId=current_user.Id,
            FechaCreacion=datetime.now()
        )
        
        db.session.add(new_equipo)
        db.session.commit()
        
        return jsonify({'message': 'Equipo creado exitosamente', 'Id': new_equipo.Id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

@inventory_bp.route('/equipos/<int:equipo_id>', methods=['PUT'])
@token_required
@requires_permission('inventory:edit')
def update_equipo(current_user, equipo_id):
    data = request.get_json()
    try:
        equipo = Equipo.query.get_or_404(equipo_id)
        
        # Actualizar campos principales
        if 'CodigoEquipo' in data: equipo.CodigoEquipo = data['CodigoEquipo']
        if 'EmpresaId' in data: equipo.EmpresaId = data['EmpresaId']
        if 'UsuarioAsignadoId' in data: equipo.UsuarioAsignadoId = data['UsuarioAsignadoId']
        if 'EstadoEquipoId' in data: equipo.EstadoEquipoId = data['EstadoEquipoId']
        if 'TipoEquipoId' in data: equipo.TipoEquipoId = data['TipoEquipoId']
        if 'FabricanteId' in data: equipo.FabricanteId = data['FabricanteId']
        if 'Modelo' in data: equipo.Modelo = data['Modelo']
        if 'Serial' in data: equipo.Serial = data['Serial']
        if 'EsPropio' in data: equipo.EsPropio = data['EsPropio']
        if 'ProveedorAlquiler' in data: equipo.ProveedorAlquiler = data['ProveedorAlquiler']
        if 'CodigoAlquiler' in data: equipo.CodigoAlquiler = data['CodigoAlquiler']
        if 'SistemaOperativoId' in data: equipo.SistemaOperativoId = data['SistemaOperativoId']
        if 'LicenciaSO' in data: equipo.LicenciaSO = data['LicenciaSO']
        if 'OfimaticaId' in data: equipo.OfimaticaId = data['OfimaticaId']
        if 'NombreOfimatica' in data: equipo.NombreOfimatica = data['NombreOfimatica']
        if 'LicenciaOfimatica' in data: equipo.LicenciaOfimatica = data['LicenciaOfimatica']
        if 'AntivirusId' in data: equipo.AntivirusId = data['AntivirusId']
        if 'EquipoPertenece' in data: equipo.EquipoPertenece = data['EquipoPertenece']
        if 'NombreEnRed' in data: equipo.NombreEnRed = data['NombreEnRed']
        
        # Actualizar Relaciones Hardware
        from app.models.inventory_models import EquipoProcesador, EquipoRAM, EquipoAlmacenamiento
        
        # Procesadores
        if 'Procesadores' in data:
            EquipoProcesador.query.filter_by(EquipoId=equipo.Id).delete()
            for proc in data['Procesadores']:
                new_proc = EquipoProcesador(
                    EquipoId=equipo.Id,
                    GeneracionId=proc.get('GeneracionId')
                )
                db.session.add(new_proc)

        # RAM
        if 'MemoriasRAM' in data:
            EquipoRAM.query.filter_by(EquipoId=equipo.Id).delete()
            for ram in data['MemoriasRAM']:
                new_ram = EquipoRAM(
                    EquipoId=equipo.Id,
                    CapacidadId=ram.get('CapacidadId'),
                    BusId=ram.get('BusId'),
                    SlotNumero=ram.get('SlotNumero')
                )
                db.session.add(new_ram)

        # Almacenamiento
        if 'Almacenamiento' in data:
            EquipoAlmacenamiento.query.filter_by(EquipoId=equipo.Id).delete()
            for disk in data['Almacenamiento']:
                new_disk = EquipoAlmacenamiento(
                    EquipoId=equipo.Id,
                    ProtocoloId=disk.get('ProtocoloId'),
                    FactorFormaId=disk.get('FactorFormaId'),
                    CapacidadId=disk.get('CapacidadId'),
                    SlotNumero=disk.get('SlotNumero')
                )
                db.session.add(new_disk)

        db.session.commit()
        return jsonify({'message': 'Equipo actualizado'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400
