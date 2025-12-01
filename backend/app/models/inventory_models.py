from app.extensions import db
from datetime import datetime

# --- HARDWARE CATALOGS ---
class MarcaProcesador(db.Model):
    __tablename__ = 'MarcaProcesador'
    Id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))

class TipoProcesador(db.Model):
    __tablename__ = 'TipoProcesador'
    Id = db.Column(db.Integer, primary_key=True)
    MarcaId = db.Column(db.Integer, db.ForeignKey('MarcaProcesador.Id'))
    Nombre = db.Column(db.String(50))

class GeneracionProcesador(db.Model):
    __tablename__ = 'GeneracionProcesador'
    Id = db.Column(db.Integer, primary_key=True)
    TipoId = db.Column(db.Integer, db.ForeignKey('TipoProcesador.Id'))
    Nombre = db.Column(db.String(50))

class TipoRAM(db.Model):
    __tablename__ = 'TipoRAM'
    Id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))
    Activo = db.Column(db.Boolean, default=True)

class CapacidadRAM(db.Model):
    __tablename__ = 'CapacidadRAM'
    Id = db.Column(db.Integer, primary_key=True)
    Capacidad = db.Column(db.String(50))
    Activo = db.Column(db.Boolean, default=True)

class BusRAM(db.Model):
    __tablename__ = 'BusRAM'
    Id = db.Column(db.Integer, primary_key=True)
    TipoId = db.Column(db.Integer, db.ForeignKey('TipoRAM.Id'))
    Velocidad = db.Column(db.String(50))
    Activo = db.Column(db.Boolean, default=True)

class TipoAlmacenamiento(db.Model):
    __tablename__ = 'TipoAlmacenamiento'
    Id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))
    Activo = db.Column(db.Boolean, default=True)

class CapacidadAlmacenamiento(db.Model):
    __tablename__ = 'CapacidadAlmacenamiento'
    Id = db.Column(db.Integer, primary_key=True)
    Capacidad = db.Column(db.String(50))
    Activo = db.Column(db.Boolean, default=True)

class ProtocoloAlmacenamiento(db.Model):
    __tablename__ = 'ProtocoloAlmacenamiento'
    Id = db.Column(db.Integer, primary_key=True)
    TipoId = db.Column(db.Integer, db.ForeignKey('TipoAlmacenamiento.Id'))
    Nombre = db.Column(db.String(50))
    Activo = db.Column(db.Boolean, default=True)

class FactorFormaAlmacenamiento(db.Model):
    __tablename__ = 'FactorFormaAlmacenamiento'
    Id = db.Column(db.Integer, primary_key=True)
    TipoId = db.Column(db.Integer, db.ForeignKey('TipoAlmacenamiento.Id'))
    Nombre = db.Column(db.String(50))
    Activo = db.Column(db.Boolean, default=True)

# --- EQUIPOS Y DETALLES ---

class Equipo(db.Model):
    __tablename__ = 'Equipos'
    Id = db.Column(db.Integer, primary_key=True)
    CodigoEquipo = db.Column(db.String(50), unique=True, nullable=False)
    EmpresaId = db.Column(db.Integer, db.ForeignKey('Empresas.Id'))
    UsuarioAsignadoId = db.Column(db.Integer, db.ForeignKey('Personas.Id'))
    
    EstadoEquipoId = db.Column(db.Integer, db.ForeignKey('EstadoEquipo.Id'))
    TipoEquipoId = db.Column(db.Integer, db.ForeignKey('TipoEquipo.Id'))
    FabricanteId = db.Column(db.Integer, db.ForeignKey('Fabricantes.Id'))
    Modelo = db.Column(db.String(100))
    Serial = db.Column(db.String(100))
    FotoSerialUrl = db.Column(db.String(500))
    
    EsPropio = db.Column(db.Boolean, default=True)
    ProveedorAlquiler = db.Column(db.String(100))
    CodigoAlquiler = db.Column(db.String(100))
    
    SistemaOperativoId = db.Column(db.Integer, db.ForeignKey('SistemasOperativos.Id'))
    LicenciaSO = db.Column(db.String(100))
    OfimaticaId = db.Column(db.Integer, db.ForeignKey('Ofimaticas.Id'))
    NombreOfimatica = db.Column(db.String(100))
    LicenciaOfimatica = db.Column(db.String(100))
    AntivirusId = db.Column(db.Integer, db.ForeignKey('Antivirus.Id'))
    
    EquipoPertenece = db.Column(db.String(20))
    NombreEnRed = db.Column(db.String(100))
    UltimoMantenimiento = db.Column(db.DateTime)
    
    FechaCreacion = db.Column(db.DateTime, default=datetime.now)
    CreadoPorId = db.Column(db.Integer)

class EquipoProcesador(db.Model):
    __tablename__ = 'EquipoProcesadores'
    Id = db.Column(db.Integer, primary_key=True)
    EquipoId = db.Column(db.Integer, db.ForeignKey('Equipos.Id'))
    GeneracionId = db.Column(db.Integer, db.ForeignKey('GeneracionProcesador.Id'))

class EquipoRAM(db.Model):
    __tablename__ = 'EquipoRAM'
    Id = db.Column(db.Integer, primary_key=True)
    EquipoId = db.Column(db.Integer, db.ForeignKey('Equipos.Id'))
    CapacidadId = db.Column(db.Integer, db.ForeignKey('CapacidadRAM.Id'))
    BusId = db.Column(db.Integer, db.ForeignKey('BusRAM.Id'))
    SlotNumero = db.Column(db.Integer)

class EquipoAlmacenamiento(db.Model):
    __tablename__ = 'EquipoAlmacenamiento'
    Id = db.Column(db.Integer, primary_key=True)
    EquipoId = db.Column(db.Integer, db.ForeignKey('Equipos.Id'))
    ProtocoloId = db.Column(db.Integer, db.ForeignKey('ProtocoloAlmacenamiento.Id'))
    FactorFormaId = db.Column(db.Integer, db.ForeignKey('FactorFormaAlmacenamiento.Id'))
    CapacidadId = db.Column(db.Integer, db.ForeignKey('CapacidadAlmacenamiento.Id'))
    SlotNumero = db.Column(db.Integer)

class EquipoAplicacion(db.Model):
    __tablename__ = 'EquipoAplicaciones'
    Id = db.Column(db.Integer, primary_key=True)
    EquipoId = db.Column(db.Integer, db.ForeignKey('Equipos.Id'))
    NombreAplicacion = db.Column(db.String(150))
    Version = db.Column(db.String(50))
    FechaInstalacion = db.Column(db.DateTime, default=datetime.now)

class EquipoAdjunto(db.Model):
    __tablename__ = 'EquipoAdjuntos'
    Id = db.Column(db.Integer, primary_key=True)
    EquipoId = db.Column(db.Integer, db.ForeignKey('Equipos.Id'))
    TipoArchivo = db.Column(db.String(20))
    RutaArchivo = db.Column(db.String(500))
    FechaSubida = db.Column(db.DateTime, default=datetime.now)
