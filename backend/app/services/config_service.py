from app.extensions import db
from app.models.core_models import (
    Empresa, Sede, Area, Cargo, 
    EstadoEquipo, TipoEquipo, Fabricante, Modelo, Puerto, SistemaOperativo, Ofimatica, Antivirus, Aplicacion
)
from app.models.inventory_models import (
    MarcaProcesador, TipoProcesador, GeneracionProcesador,
    TipoRAM, CapacidadRAM, BusRAM,
    TipoAlmacenamiento, CapacidadAlmacenamiento, ProtocoloAlmacenamiento, FactorFormaAlmacenamiento
)
from app.models.auth_models import Persona, Rol, Permiso
from werkzeug.security import generate_password_hash

# Mapa de nombres de catálogo a Modelos SQLAlchemy
CATALOG_MODELS = {
    'areas': Area,
    'cargos': Cargo,
    'estados_equipo': EstadoEquipo,
    'tipos_equipo': TipoEquipo,
    'fabricantes': Fabricante,
    'modelos': Modelo,
    'puertos': Puerto,
    'sistemas_operativos': SistemaOperativo,
    'ofimaticas': Ofimatica,
    'antivirus': Antivirus,
    'marcas_procesador': MarcaProcesador,
    'tipos_procesador': TipoProcesador,
    'generaciones_procesador': GeneracionProcesador,
    'tipos_ram': TipoRAM,
    'capacidades_ram': CapacidadRAM,
    'buses_ram': BusRAM,
    'tipos_almacenamiento': TipoAlmacenamiento,
    'capacidades_almacenamiento': CapacidadAlmacenamiento,
    'protocolos_almacenamiento': ProtocoloAlmacenamiento,
    'factores_forma_almacenamiento': FactorFormaAlmacenamiento,
    'aplicaciones': Aplicacion
}

class ConfigService:
    
    # --- EMPRESAS ---
    @staticmethod
    def get_all_companies():
        return Empresa.query.all()
    
    @staticmethod
    def get_company_by_id(company_id):
        return Empresa.query.get(company_id)
        
    @staticmethod
    def create_company(data):
        new_company = Empresa(
            NIT=data.get('NIT'),
            RazonSocial=data.get('RazonSocial'),
            Direccion=data.get('Direccion'),
            Telefono=data.get('Telefono'),
            EsCliente=data.get('EsCliente', True),
            CiudadId=data.get('CiudadId')
        )
        db.session.add(new_company)
        db.session.commit()
        return new_company

    @staticmethod
    def update_company(company_id, data):
        company = Empresa.query.get(company_id)
        if not company:
            return None
            
        company.RazonSocial = data.get('RazonSocial', company.RazonSocial)
        company.Direccion = data.get('Direccion', company.Direccion)
        company.Telefono = data.get('Telefono', company.Telefono)
        company.CiudadId = data.get('CiudadId', company.CiudadId)
        company.EsCliente = data.get('EsCliente', company.EsCliente)
        
        # Si se desactiva la empresa, desactivar todas sus sedes
        new_activo = data.get('Activo')
        if new_activo is not None:
            company.Activo = new_activo
            if not new_activo:
                sedes = Sede.query.filter_by(EmpresaId=company.Id).all()
                for sede in sedes:
                    sede.Activo = False
        
        db.session.commit()
        return company

    # --- SEDES ---
    @staticmethod
    def get_sedes(filters=None):
        query = Sede.query
        if filters:
            if 'EmpresaId' in filters:
                query = query.filter_by(EmpresaId=filters['EmpresaId'])
        return query.all()

    @staticmethod
    def create_sede(data):
        # Validar que la empresa esté activa
        empresa = Empresa.query.get(data.get('EmpresaId'))
        if not empresa or not empresa.Activo:
            raise ValueError("No se puede crear una sede para una empresa inactiva")

        new_sede = Sede(
            EmpresaId=data.get('EmpresaId'),
            NombreSede=data.get('NombreSede'),
            Direccion=data.get('Direccion'),
            CiudadId=data.get('CiudadId'),
            Telefono=data.get('Telefono'),
            Activo=True
        )
        db.session.add(new_sede)
        db.session.commit()
        return new_sede

    @staticmethod
    def update_sede(sede_id, data):
        sede = Sede.query.get(sede_id)
        if not sede:
            return None
        
        sede.NombreSede = data.get('NombreSede', sede.NombreSede)
        sede.Direccion = data.get('Direccion', sede.Direccion)
        sede.CiudadId = data.get('CiudadId', sede.CiudadId)
        sede.Telefono = data.get('Telefono', sede.Telefono)
        
        # Validar activación
        new_activo = data.get('Activo')
        if new_activo is not None:
            if new_activo and not sede.Activo: # Intentando activar
                empresa = Empresa.query.get(sede.EmpresaId)
                if not empresa or not empresa.Activo:
                    raise ValueError("No se puede activar la sede porque la empresa está inactiva")
            sede.Activo = new_activo
        
        db.session.commit()
        return sede

    # --- PERMISOS ---
    @staticmethod
    def get_all_permissions():
        return Permiso.query.order_by(Permiso.Modulo, Permiso.Codigo).all()

    # --- ROLES ---
    @staticmethod
    def get_all_roles():
        return Rol.query.order_by(Rol.Nombre).all()

    # --- USUARIOS ---
    @staticmethod
    def get_users(filters=None):
        query = Persona.query
        if filters:
            if 'EsUsuarioSistema' in filters:
                query = query.filter_by(EsUsuarioSistema=filters['EsUsuarioSistema'])
            if 'EmpresaId' in filters:
                # TODO: Filtrar por empresa si implementamos relación Persona-Empresa directa o vía Sede
                pass
        return query.all()

    @staticmethod
    def create_user(data):
        # Verificar correo
        if Persona.query.filter_by(Correo=data['Correo']).first():
            raise ValueError("El correo ya existe")

        new_user = Persona(
            Nombre=data['Nombre'],
            Apellido=data['Apellido'],
            Documento=data.get('Documento'),
            Correo=data['Correo'],
            Celular=data.get('Celular'),
            CargoId=data.get('CargoId'),
            AreaId=data.get('AreaId'),
            SedeId=data.get('SedeId'),
            RolId=data.get('RolId'),
            EsUsuarioSistema=data.get('EsUsuarioSistema', False),
            Activo=True
        )
        
        if new_user.EsUsuarioSistema and data.get('Password'):
            new_user.PasswordHash = generate_password_hash(data['Password'])
            
        # Asignar permisos específicos
        if 'PermisosEspecificos' in data:
            permisos_ids = data['PermisosEspecificos']
            permisos = Permiso.query.filter(Permiso.Id.in_(permisos_ids)).all()
            new_user.PermisosEspecificos = permisos

        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def update_user(user_id, data):
        user = Persona.query.get(user_id)
        if not user:
            return None

        user.Nombre = data.get('Nombre', user.Nombre)
        user.Apellido = data.get('Apellido', user.Apellido)
        user.Documento = data.get('Documento', user.Documento)
        user.Celular = data.get('Celular', user.Celular)
        user.CargoId = data.get('CargoId', user.CargoId)
        user.AreaId = data.get('AreaId', user.AreaId)
        user.SedeId = data.get('SedeId', user.SedeId)
        user.RolId = data.get('RolId', user.RolId)
        user.Activo = data.get('Activo', user.Activo)
        
        if data.get('Password'):
            user.PasswordHash = generate_password_hash(data['Password'])
            
        # Actualizar permisos específicos
        if 'PermisosEspecificos' in data:
            permisos_ids = data['PermisosEspecificos']
            permisos = Permiso.query.filter(Permiso.Id.in_(permisos_ids)).all()
            user.PermisosEspecificos = permisos
            
        db.session.commit()
        return user

    # --- CATÁLOGOS GENÉRICOS ---
    @staticmethod
    def get_catalog_items(catalog_name, filters=None):
        model = CATALOG_MODELS.get(catalog_name)
        if not model:
            raise ValueError("Catálogo no válido")
        
        query = model.query
        if filters:
            for key, value in filters.items():
                if hasattr(model, key):
                    query = query.filter(getattr(model, key) == value)
                    
        return query.all()
        
    @staticmethod
    def create_catalog_item(catalog_name, data):
        model = CATALOG_MODELS.get(catalog_name)
        if not model:
            raise ValueError("Catálogo no válido")
            
        # Asumimos que la mayoría tiene 'Nombre'
        # Para tablas con dependencias (ej: TipoProcesador necesita MarcaId), 
        # data debe traer la FK.
        new_item = model(**data)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    @staticmethod
    def update_catalog_item(catalog_name, item_id, data):
        model = CATALOG_MODELS.get(catalog_name)
        if not model:
            raise ValueError("Catálogo no válido")
            
        item = model.query.get(item_id)
        if not item:
            return None
            
        # Actualización genérica de campos comunes
        if 'Nombre' in data and hasattr(item, 'Nombre'):
            item.Nombre = data['Nombre']
        if 'Activo' in data and hasattr(item, 'Activo'):
            item.Activo = data['Activo']
            
        # Campos específicos (se pueden agregar más según necesidad)
        if 'Capacidad' in data and hasattr(item, 'Capacidad'):
            item.Capacidad = data['Capacidad']
        if 'Velocidad' in data and hasattr(item, 'Velocidad'):
            item.Velocidad = data['Velocidad']
            
        db.session.commit()
        return item
