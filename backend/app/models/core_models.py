from app.extensions import db

# --- GEOGRAFÍA ---
class Departamento(db.Model):
    __tablename__ = 'Departamentos'
    Id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100), nullable=False)

class Ciudad(db.Model):
    __tablename__ = 'Ciudades'
    Id = db.Column(db.Integer, primary_key=True)
    DepartamentoId = db.Column(db.Integer, db.ForeignKey('Departamentos.Id'))
    Nombre = db.Column(db.String(100), nullable=False)

# --- ESTRUCTURA EMPRESARIAL ---
class Empresa(db.Model):
    __tablename__ = 'Empresas'
    Id = db.Column(db.Integer, primary_key=True)
    NIT = db.Column(db.String(20), unique=True, nullable=False)
    RazonSocial = db.Column(db.String(150), nullable=False)
    Direccion = db.Column(db.String(200))
    CiudadId = db.Column(db.Integer, db.ForeignKey('Ciudades.Id'))
    Telefono = db.Column(db.String(20))
    EsCliente = db.Column(db.Boolean, default=False)
    Activo = db.Column(db.Boolean, default=True)

class Sede(db.Model):
    __tablename__ = 'Sedes'
    Id = db.Column(db.Integer, primary_key=True)
    EmpresaId = db.Column(db.Integer, db.ForeignKey('Empresas.Id'))
    NombreSede = db.Column(db.String(100), nullable=False)
    Direccion = db.Column(db.String(200))
    CiudadId = db.Column(db.Integer, db.ForeignKey('Ciudades.Id'))
    Telefono = db.Column(db.String(20))
    Activo = db.Column(db.Boolean, default=True)

class Area(db.Model):
    __tablename__ = 'Areas'
    Id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100))
    Activo = db.Column(db.Boolean, default=True)

class Cargo(db.Model):
    __tablename__ = 'Cargos'
    Id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100))
    Activo = db.Column(db.Boolean, default=True)

# --- CATÁLOGOS GLOBALES ---
class EstadoEquipo(db.Model):
    __tablename__ = 'EstadoEquipo'
    Id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))
    Activo = db.Column(db.Boolean, default=True)

class TipoEquipo(db.Model):
    __tablename__ = 'TipoEquipo'
    Id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))
    Activo = db.Column(db.Boolean, default=True)

class Fabricante(db.Model):
    __tablename__ = 'Fabricantes'
    Id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))
    Activo = db.Column(db.Boolean, default=True)

class Modelo(db.Model):
    __tablename__ = 'Modelos'
    Id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100))
    Activo = db.Column(db.Boolean, default=True)

class Puerto(db.Model):
    __tablename__ = 'Puertos'
    Id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))
    Activo = db.Column(db.Boolean, default=True)

class SistemaOperativo(db.Model):
    __tablename__ = 'SistemasOperativos'
    Id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100))
    Activo = db.Column(db.Boolean, default=True)

class Ofimatica(db.Model):
    __tablename__ = 'Ofimaticas'
    Id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100))
    Activo = db.Column(db.Boolean, default=True)

class Antivirus(db.Model):
    __tablename__ = 'Antivirus'
    Id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100))
    Activo = db.Column(db.Boolean, default=True)

class Aplicacion(db.Model):
    __tablename__ = 'Aplicaciones'
    Id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100))
    Version = db.Column(db.String(50))
    Activo = db.Column(db.Boolean, default=True)


