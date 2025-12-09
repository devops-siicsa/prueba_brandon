from flask import Blueprint, request, jsonify, g
from app.extensions import db
from app.models.inventory_models import Equipo
from app.utils.decorators import token_required, requires_permission
from datetime import datetime
import os
from werkzeug.utils import secure_filename
from flask import current_app, send_from_directory

inventory_bp = Blueprint('inventory', __name__, url_prefix='/api/inventory')

# --- EQUIPOS ---

from app.models.core_models import Empresa

@inventory_bp.route('/equipos', methods=['GET'])
@token_required
def get_equipos(current_user):
    try:
        # Filtros básicos
        empresa_id = request.args.get('EmpresaId')
        sede_id = request.args.get('SedeId')
        
        # Join with Persona to get Assigned User Name
        from app.models.auth_models import Persona
        query = db.session.query(
            Equipo, 
            Empresa.RazonSocial,
            Persona.Nombre, 
            Persona.Apellido
        ).outerjoin(Empresa, Equipo.EmpresaId == Empresa.Id)\
         .outerjoin(Persona, Equipo.UsuarioAsignadoId == Persona.Id)
        
        if empresa_id:
            query = query.filter(Equipo.EmpresaId == empresa_id)
        
        codigo = request.args.get('CodigoEquipo')
        if codigo:
            query = query.filter(Equipo.CodigoEquipo == codigo)
            
        results = query.order_by(Equipo.FechaCreacion.desc()).all()
        
        return jsonify([{
            'Id': e.Id,
            'CodigoEquipo': e.CodigoEquipo,
            'EmpresaId': e.EmpresaId,
            'EmpresaNombre': empresa_nombre,
            'SedeId': e.SedeId,
            'UsuarioAsignadoId': e.UsuarioAsignadoId,
            'UsuarioNombre': f"{nombre_persona} {apellido_persona}" if nombre_persona and apellido_persona else None,
            'EstadoEquipoId': e.EstadoEquipoId,
            'TipoEquipoId': e.TipoEquipoId,
            'FabricanteId': e.FabricanteId,
            'Modelo': e.Modelo,
            'Serial': e.Serial,
            'FechaCreacion': e.FechaCreacion.isoformat() if e.FechaCreacion else None
        } for e, empresa_nombre, nombre_persona, apellido_persona in results]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@inventory_bp.route('/equipos/<int:equipo_id>', methods=['GET'])
@token_required
def get_equipo_detail(current_user, equipo_id):
    try:
        equipo = Equipo.query.get_or_404(equipo_id)
        
        # Cargar relaciones
        from app.models.inventory_models import EquipoProcesador, EquipoRAM, EquipoAlmacenamiento, EquipoAplicacion, EquipoAdjunto
        
        procesadores = EquipoProcesador.query.filter_by(EquipoId=equipo.Id).all()
        memorias = EquipoRAM.query.filter_by(EquipoId=equipo.Id).all()
        discos = EquipoAlmacenamiento.query.filter_by(EquipoId=equipo.Id).all()
        apps = EquipoAplicacion.query.filter_by(EquipoId=equipo.Id).all()
        
        return jsonify({
            'Id': equipo.Id,
            'CodigoEquipo': equipo.CodigoEquipo,
            'EmpresaId': equipo.EmpresaId,
            'SedeId': equipo.SedeId,
            'UsuarioAsignadoId': equipo.UsuarioAsignadoId,
            'UsuarioNombre': equipo.UsuarioAsignado.Nombre if equipo.UsuarioAsignadoId and hasattr(equipo, 'UsuarioAsignado') and equipo.UsuarioAsignado else None,
            'UsuarioApellido': equipo.UsuarioAsignado.Apellido if equipo.UsuarioAsignadoId and hasattr(equipo, 'UsuarioAsignado') and equipo.UsuarioAsignado else None,
            'Cargo': equipo.UsuarioAsignado.Cargo.Nombre if equipo.UsuarioAsignadoId and hasattr(equipo, 'UsuarioAsignado') and equipo.UsuarioAsignado and equipo.UsuarioAsignado.Cargo else None,
            'Area': equipo.UsuarioAsignado.Area.Nombre if equipo.UsuarioAsignadoId and hasattr(equipo, 'UsuarioAsignado') and equipo.UsuarioAsignado and equipo.UsuarioAsignado.Area else None,
            'Correo': equipo.UsuarioAsignado.Correo if equipo.UsuarioAsignadoId and hasattr(equipo, 'UsuarioAsignado') and equipo.UsuarioAsignado else None,
            'Telefono': equipo.UsuarioAsignado.Celular if equipo.UsuarioAsignadoId and hasattr(equipo, 'UsuarioAsignado') and equipo.UsuarioAsignado else None,
            'Ciudad': equipo.Sede.Ciudad.Nombre if equipo.SedeId and hasattr(equipo, 'Sede') and equipo.Sede and equipo.Sede.Ciudad else None,
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
            'NombreGrupoDominio': equipo.NombreGrupoDominio,
            'NombreEnRed': equipo.NombreEnRed,
            'UltimoMantenimiento': equipo.UltimoMantenimiento.isoformat() if equipo.UltimoMantenimiento else None,
            'FechaCreacion': equipo.FechaCreacion.isoformat() if equipo.FechaCreacion else None,
            'CreadoPorId': equipo.CreadoPorId,
            
            # Detalles Hardware
            'Procesadores': [{
                'Id': p.Id, 
                'GeneracionId': p.GeneracionId,
                'MarcaId': p.Generacion.Tipo.MarcaId if p.Generacion and p.Generacion.Tipo else None,
                'TipoId': p.Generacion.TipoId if p.Generacion else None
            } for p in procesadores],
            'MemoriasRAM': [{
                'Id': m.Id, 
                'CapacidadId': m.CapacidadId, 
                'BusId': m.BusId, 
                'SlotNumero': m.SlotNumero,
                'TipoId': m.Bus.TipoId if m.Bus else None
            } for m in memorias],
            'Almacenamiento': [{
                'Id': d.Id, 
                'ProtocoloId': d.ProtocoloId, 
                'FactorFormaId': d.FactorFormaId, 
                'CapacidadId': d.CapacidadId, 
                'SlotNumero': d.SlotNumero,
                'TipoId': d.Protocolo.TipoId if d.Protocolo else None
            } for d in discos],

            'Aplicativos': [{'Id': a.Id, 'Nombre': a.NombreAplicacion, 'Version': a.Version} for a in apps],
            'Adjuntos': [{
                'Id': adj.Id,
                'name': os.path.basename(adj.RutaArchivo),
                'type': adj.TipoArchivo, # MIME type logic needed if stored simply as ext
                'path': adj.RutaArchivo
            } for adj in EquipoAdjunto.query.filter_by(EquipoId=equipo.Id).all()]
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
            SedeId=data.get('SedeId'),
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
            NombreGrupoDominio=data.get('NombreGrupoDominio'),
            NombreEnRed=data.get('NombreEnRed'),
            Distribucion=data.get('Distribucion'),
            DistribucionOfimatica=data.get('DistribucionOfimatica'),
            CreadoPorId=current_user.Id,
            FechaCreacion=datetime.now()
        )
        
        db.session.add(new_equipo)
        db.session.flush() # Flush to get Id for relationships

        # Handle Apps (Aplicativos)
        if 'Aplicativos' in data and isinstance(data['Aplicativos'], list):
             from app.models.core_models import Aplicacion
             from app.models.inventory_models import EquipoAplicacion
             
             for app_id in data['Aplicativos']:
                 app_catalog = Aplicacion.query.get(app_id)
                 if app_catalog:
                     new_app_rel = EquipoAplicacion(
                         EquipoId=new_equipo.Id,
                         NombreAplicacion=app_catalog.Nombre,
                         Version=app_catalog.Version
                     )
                     db.session.add(new_app_rel)

        # Handle Hardware (Procesadores, RAM, Discos)
        from app.models.inventory_models import EquipoProcesador, EquipoRAM, EquipoAlmacenamiento

        if 'Procesadores' in data:
            for proc in data['Procesadores']:
                new_proc = EquipoProcesador(
                    EquipoId=new_equipo.Id,
                    GeneracionId=proc.get('GeneracionId')
                )
                db.session.add(new_proc)

        if 'MemoriasRAM' in data:
            for ram in data['MemoriasRAM']:
                # Frontend uses VelocidadId for BusId
                bus_id = ram.get('BusId') or ram.get('VelocidadId')
                new_ram = EquipoRAM(
                    EquipoId=new_equipo.Id,
                    CapacidadId=ram.get('CapacidadId'),
                    BusId=bus_id,
                    SlotNumero=ram.get('SlotNumero')
                )
                db.session.add(new_ram)

        if 'Almacenamiento' in data:
            for disk in data['Almacenamiento']:
                new_disk = EquipoAlmacenamiento(
                    EquipoId=new_equipo.Id,
                    ProtocoloId=disk.get('ProtocoloId'),
                    FactorFormaId=disk.get('FactorFormaId'),
                    CapacidadId=disk.get('CapacidadId'),
                    SlotNumero=disk.get('SlotNumero')
                )
                db.session.add(new_disk)

        db.session.commit()
        return jsonify({'message': 'Equipo creado exitosamente', 'Id': new_equipo.Id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

@inventory_bp.route('/equipos/<int:equipo_id>', methods=['PUT'])
@token_required
@requires_permission('equipment:edit_all')
def update_equipo(current_user, equipo_id):
    data = request.get_json()
    try:
        equipo = Equipo.query.get(equipo_id)
        if not equipo:
            return jsonify({'message': 'Equipo no encontrado'}), 404

        # Actualizar campos principales
        if 'CodigoEquipo' in data: equipo.CodigoEquipo = data['CodigoEquipo']
        if 'EmpresaId' in data: equipo.EmpresaId = data['EmpresaId']
        if 'SedeId' in data: equipo.SedeId = data['SedeId']
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
        if 'NombreGrupoDominio' in data: equipo.NombreGrupoDominio = data['NombreGrupoDominio']
        if 'NombreEnRed' in data: equipo.NombreEnRed = data['NombreEnRed']
        if 'Distribucion' in data: equipo.Distribucion = data['Distribucion']
        if 'DistribucionOfimatica' in data: equipo.DistribucionOfimatica = data['DistribucionOfimatica']
        
        # --- Actualizar Datos de Persona (Responsable) ---
        # Si el equipo tiene usuario asignado, intentamos actualizar sus datos
        if equipo.UsuarioAsignadoId:
            from app.models.auth_models import Persona
            from app.models.core_models import Cargo, Area
            persona = Persona.query.get(equipo.UsuarioAsignadoId)
            
            if persona:
                import json
                changes = {}
                
                # Nombre
                if 'UsuarioNombre' in data and data['UsuarioNombre'] != persona.Nombre:
                    changes['Nombre'] = {'antes': persona.Nombre, 'despues': data['UsuarioNombre']}
                    persona.Nombre = data['UsuarioNombre']

                # Apellido
                if 'UsuarioApellido' in data and data['UsuarioApellido'] != persona.Apellido:
                    changes['Apellido'] = {'antes': persona.Apellido, 'despues': data['UsuarioApellido']}
                    persona.Apellido = data['UsuarioApellido']

                # Correo logic with Smart Reassignment
                if 'Correo' in data and data['Correo'] != persona.Correo:
                     existing_persona = Persona.query.filter_by(Correo=data['Correo']).first()
                     if existing_persona and existing_persona.Id != persona.Id:
                         # Smart Reassignment: User found, assign equipment to them
                         equipo.UsuarioAsignadoId = existing_persona.Id
                         persona = existing_persona # Switch context to update the NEW user if needed
                         # Don't log 'email change' for the old user
                     else:
                         # Normal update
                         changes['Correo'] = {'antes': persona.Correo, 'despues': data['Correo']}
                         persona.Correo = data['Correo']

                # Telefono
                if 'Telefono' in data and data['Telefono'] != persona.Celular:
                    changes['Telefono'] = {'antes': persona.Celular, 'despues': data['Telefono']}
                    persona.Celular = data['Telefono']
                
                # Cargo (Lookup/Create)
                if 'Cargo' in data and data['Cargo']:
                    cargo_input = data['Cargo']
                    cargo_nombre = None
                    if isinstance(cargo_input, dict):
                        cargo_nombre = cargo_input.get('Nombre')
                    elif isinstance(cargo_input, str):
                        cargo_nombre = cargo_input
                        
                    if cargo_nombre:
                        cargo_nombre = cargo_nombre.strip()
                        current_cargo_name = persona.Cargo.Nombre if persona.Cargo else None
                        
                        if current_cargo_name != cargo_nombre:
                            # Changes detected
                            changes['Cargo'] = {'antes': current_cargo_name, 'despues': cargo_nombre}

                            # Find existing or create
                            cargo_obj = Cargo.query.filter(Cargo.Nombre.ilike(cargo_nombre)).first()
                            if not cargo_obj:
                                cargo_obj = Cargo(Nombre=cargo_nombre, Activo=True)
                                db.session.add(cargo_obj)
                                db.session.flush() # Get Id
                            persona.CargoId = cargo_obj.Id

                # Area (Lookup/Create)
                if 'Area' in data and data['Area']:
                    area_input = data['Area']
                    area_nombre = None
                    if isinstance(area_input, dict):
                        area_nombre = area_input.get('Nombre')
                    elif isinstance(area_input, str):
                        area_nombre = area_input
                        
                    if area_nombre:
                        area_nombre = area_nombre.strip()
                        current_area_name = persona.Area.Nombre if persona.Area else None
                        
                        if current_area_name != area_nombre:
                            changes['Area'] = {'antes': current_area_name, 'despues': area_nombre}

                            area_obj = Area.query.filter(Area.Nombre.ilike(area_nombre)).first()
                            if not area_obj:
                                area_obj = Area(Nombre=area_nombre, Activo=True)
                                db.session.add(area_obj)
                                db.session.flush()
                            persona.AreaId = area_obj.Id

                if changes:
                    # Manually log this 'User Update' linked to the Equipment so it appears in history
                    from app.models.audit_models import AuditoriaLog
                    from datetime import datetime
                    
                    detalle_json = json.dumps(changes)
                    
                    audit_log = AuditoriaLog(
                         TablaAfectada='Equipos', # Link to Equipos table so it shows in history
                         RegistroId=equipo.Id,
                         Accion='EDITAR',
                         UsuarioId=g.current_user.Id if hasattr(g, 'current_user') else None,
                         Fecha=datetime.now(),
                         DetalleCambio=detalle_json,
                         CampoAfectado='Datos Usuario',
                         ValorAntes='Datos Previos',
                         ValorDespues='Actualizado'
                    )
                    db.session.add(audit_log)
                    db.session.add(persona) # Mark for update
        
        # Actualizar Relaciones Hardware
        from app.models.inventory_models import EquipoProcesador, EquipoRAM, EquipoAlmacenamiento
        
        # Procesadores
        if 'Procesadores' in data:
            current_procs = EquipoProcesador.query.filter_by(EquipoId=equipo.Id).order_by(EquipoProcesador.Id).all()
            incoming_data = data['Procesadores']
            
            for i, proc_data in enumerate(incoming_data):
                gen_id = proc_data.get('GeneracionId')
                if not gen_id: continue

                if i < len(current_procs):
                    existing = current_procs[i]
                    if existing.GeneracionId != gen_id:
                        existing.GeneracionId = gen_id
                else:
                    new_proc = EquipoProcesador(EquipoId=equipo.Id, GeneracionId=gen_id)
                    db.session.add(new_proc)
            
            if len(incoming_data) < len(current_procs):
                for j in range(len(incoming_data), len(current_procs)):
                    db.session.delete(current_procs[j])

        # RAM
        if 'MemoriasRAM' in data:
            current_rams = EquipoRAM.query.filter_by(EquipoId=equipo.Id).all()
            current_map = {r.SlotNumero: r for r in current_rams}
            
            incoming_slots = set()

            for ram in data['MemoriasRAM']:
                 slot = int(ram.get('SlotNumero') or 0)
                 cap_id = ram.get('CapacidadId')
                 bus_id = ram.get('BusId') or ram.get('VelocidadId')

                 if not slot or not cap_id or not bus_id:
                     continue
                 
                 incoming_slots.add(slot)

                 if slot in current_map:
                     # Update existing
                     existing = current_map[slot]
                     if existing.CapacidadId != cap_id or existing.BusId != bus_id:
                         existing.CapacidadId = cap_id
                         existing.BusId = bus_id
                         # Helper for audit to know about this object's relationships if needed
                 else:
                     # Create new
                     new_ram = EquipoRAM(
                         EquipoId=equipo.Id,
                         CapacidadId=cap_id,
                         BusId=bus_id,
                         SlotNumero=slot
                     )
                     db.session.add(new_ram)
            
            # Delete removed slots
            for slot, existing in current_map.items():
                if slot not in incoming_slots:
                    db.session.delete(existing)

        # Almacenamiento
        if 'Almacenamiento' in data:
            current_disks = EquipoAlmacenamiento.query.filter_by(EquipoId=equipo.Id).all()
            # Map by SlotNumero for smart update
            current_map = {d.SlotNumero: d for d in current_disks}
            
            incoming_slots = set()

            for disk in data['Almacenamiento']:
                slot = int(disk.get('SlotNumero') or 0)
                proto_id = disk.get('ProtocoloId')
                ff_id = disk.get('FactorFormaId')
                cap_id = disk.get('CapacidadId')

                if not slot or not cap_id: # Minimal requirements
                    continue
                
                incoming_slots.add(slot)

                if slot in current_map:
                    # Update existing
                    existing = current_map[slot]
                    if (existing.ProtocoloId != proto_id or 
                        existing.FactorFormaId != ff_id or 
                        existing.CapacidadId != cap_id):
                        
                        existing.ProtocoloId = proto_id
                        existing.FactorFormaId = ff_id
                        existing.CapacidadId = cap_id
                else:
                    # Create new
                    new_disk = EquipoAlmacenamiento(
                        EquipoId=equipo.Id,
                        ProtocoloId=proto_id,
                        FactorFormaId=ff_id,
                        CapacidadId=cap_id,
                        SlotNumero=slot
                    )
                    db.session.add(new_disk)
            
            # Delete removed slots
            for slot, existing in current_map.items():
                if slot not in incoming_slots:
                    db.session.delete(existing)

        # Aplicativos (Apps) - Update
        if 'Aplicativos' in data and isinstance(data['Aplicativos'], list):
             from app.models.inventory_models import EquipoAplicacion
             from app.models.core_models import Aplicacion
             
             # Apps logic: Match by Name and Version roughly? 
             # Actually, simpler: The frontend sends the App ID if it exists?
             # In Create, we use App ID to lookup Name/Version.
             # In Update, we do the same.
             # The DB stores Name and Version copies (Snapshot).
             # We should compare the *resulting* Name/Version or just the source App IDs if available?
             # But the DB table 'EquipoAplicacion' does NOT store 'AplicacionId' (FK), strictly copies.
             # So we can only rely on the *Names* and *Versions* stored.
             # But the input `data['Aplicativos']` is a list of App Catalog IDs (integers) or dicts with Id?
             
             current_apps = EquipoAplicacion.query.filter_by(EquipoId=equipo.Id).all()
             current_app_sig = set((a.NombreAplicacion, a.Version) for a in current_apps)
             
             incoming_app_ids = []
             for app_item in data['Aplicativos']:
                 if isinstance(app_item, dict):
                     if app_item.get('Id'): incoming_app_ids.append(app_item.get('Id'))
                 else:
                     incoming_app_ids.append(app_item)
             
             # Resolve incoming IDs to Name/Version to compare
             incoming_app_sig = set()
             catalogs = Aplicacion.query.filter(Aplicacion.Id.in_(incoming_app_ids)).all() if incoming_app_ids else []
             for c in catalogs:
                 incoming_app_sig.add((c.Nombre, c.Version))
                 
             if current_app_sig != incoming_app_sig:
                 EquipoAplicacion.query.filter_by(EquipoId=equipo.Id).delete()
                 for cat in catalogs:
                     new_app_rel = EquipoAplicacion(
                         EquipoId=equipo.Id,
                         NombreAplicacion=cat.Nombre,
                         Version=cat.Version
                     )
                     db.session.add(new_app_rel)

        db.session.commit()
        return jsonify({'message': 'Equipo actualizado'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

# --- ADJUNTOS ---

@inventory_bp.route('/equipos/<int:equipo_id>/attachments', methods=['POST'])
@token_required
@requires_permission('equipment:edit_all') # Assuming editing permission required
def upload_attachment(current_user, equipo_id):
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    
    if file:
        filename = secure_filename(file.filename)
        # Unique filename to prevent overwrites
        unique_filename = f"{equipo_id}_{int(datetime.now().timestamp())}_{filename}"
        
        upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(upload_path)
        
        from app.models.inventory_models import EquipoAdjunto
        new_adjunto = EquipoAdjunto(
            EquipoId=equipo_id,
            TipoArchivo=file.content_type,
            RutaArchivo=unique_filename,
            FechaSubida=datetime.now()
        )
        db.session.add(new_adjunto)
        db.session.commit()
        
        return jsonify({
            'message': 'Archivo subido exitosamente',
            'file': {
                'Id': new_adjunto.Id,
                'name': filename,
                'type': new_adjunto.TipoArchivo,
                'size': os.path.getsize(upload_path),
                'path': unique_filename
            }
        }), 201

@inventory_bp.route('/equipos/<int:equipo_id>/attachments/<int:attachment_id>', methods=['DELETE'])
@token_required
@requires_permission('equipment:edit_all')
def delete_attachment(current_user, equipo_id, attachment_id):
    from app.models.inventory_models import EquipoAdjunto
    adjunto = EquipoAdjunto.query.get_or_404(attachment_id)
    
    if adjunto.EquipoId != equipo_id:
        return jsonify({'message': 'Adjunto no corresponde al equipo'}), 400
        
    try:
        # Delete from disk
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], adjunto.RutaArchivo)
        if os.path.exists(file_path):
            os.remove(file_path)
            
        db.session.delete(adjunto)
        db.session.commit()
        return jsonify({'message': 'Adjunto eliminado'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500

@inventory_bp.route('/equipos/<int:equipo_id>/attachments/<int:attachment_id>', methods=['GET'])
@token_required
def get_attachment(current_user, equipo_id, attachment_id):
    from app.models.inventory_models import EquipoAdjunto
    adjunto = EquipoAdjunto.query.get_or_404(attachment_id)
    
    if adjunto.EquipoId != equipo_id:
        return jsonify({'message': 'Adjunto no corresponde al equipo'}), 400
        
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], adjunto.RutaArchivo, as_attachment=False)

