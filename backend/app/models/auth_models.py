from app.extensions import db
from datetime import datetime

# Tabla intermedia para relación Many-to-Many
rol_permisos = db.Table('RolPermisos',
    db.Column('RolId', db.Integer, db.ForeignKey('Roles.Id'), primary_key=True),
    db.Column('PermisoId', db.Integer, db.ForeignKey('Permisos.Id'), primary_key=True)
)

# Tabla intermedia para relación Many-to-Many (Usuario - Permisos)
usuario_permisos = db.Table('UsuarioPermisos',
    db.Column('PersonaId', db.Integer, db.ForeignKey('Personas.Id'), primary_key=True),
    db.Column('PermisoId', db.Integer, db.ForeignKey('Permisos.Id'), primary_key=True)
)

class Permiso(db.Model):
    __tablename__ = 'Permisos'
    Id = db.Column(db.Integer, primary_key=True)
    Codigo = db.Column(db.String(100), unique=True, nullable=False)
    Descripcion = db.Column(db.String(200))
    Modulo = db.Column(db.String(150))
    SubModulo = db.Column(db.String(100), nullable=True) # Nuevo campo para subcategorías
    Activo = db.Column(db.Boolean, default=True)

class Rol(db.Model):
    __tablename__ = 'Roles'
    Id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50), unique=True, nullable=False)
    Scope = db.Column(db.String(20), nullable=False) # GLOBAL, TENANT
    Descripcion = db.Column(db.String(200))
    Activo = db.Column(db.Boolean, default=True)
    
    # Relación Many-to-Many
    Permisos = db.relationship('Permiso', secondary=rol_permisos, lazy='subquery',
        backref=db.backref('roles', lazy=True))

class Persona(db.Model):
    __tablename__ = 'Personas'
    
    Id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100), nullable=False)
    Apellido = db.Column(db.String(100), nullable=False)
    Correo = db.Column(db.String(150), unique=True, nullable=False)
    Celular = db.Column(db.String(20), default='57')
    
    # Claves foráneas
    SedeId = db.Column(db.Integer, db.ForeignKey('Sedes.Id'))
    AreaId = db.Column(db.Integer, db.ForeignKey('Areas.Id'))
    CargoId = db.Column(db.Integer, db.ForeignKey('Cargos.Id'))
    RolId = db.Column(db.Integer, db.ForeignKey('Roles.Id')) # Nuevo campo RBAC
    
    # Relaciones
    Cargo = db.relationship('Cargo', foreign_keys=[CargoId])
    Rol = db.relationship('Rol', foreign_keys=[RolId])
    
    # Relación Many-to-Many para Permisos Específicos
    PermisosEspecificos = db.relationship('Permiso', secondary=usuario_permisos, lazy='subquery',
        backref=db.backref('usuarios', lazy=True))
    
    # Campos de Login y Seguridad
    PasswordHash = db.Column(db.String(512), nullable=True) # NVARCHAR(512)
    EsUsuarioSistema = db.Column(db.Boolean, default=False)
    EsContactoCliente = db.Column(db.Boolean, default=False)
    
    # 2FA y Seguridad
    TwoFactorSecret = db.Column(db.String(100), nullable=True) # Semilla 2FA
    TwoFactorEnabled = db.Column(db.Boolean, default=False)
    
    # Control de Fuerza Bruta y Auditoría
    IntentosFallidos = db.Column(db.Integer, default=0)
    BloqueoHasta = db.Column(db.DateTime, nullable=True)
    UltimoLogin = db.Column(db.DateTime, nullable=True)
    
    Activo = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Persona {self.Nombre} {self.Apellido}>'

    def has_permission(self, permission_code):
        # 1. Super Admin tiene acceso total
        if self.Rol and self.Rol.Nombre == 'SUPER ADMINISTRADOR':
            return True
        
        # 2. Verificar en Rol
        if self.Rol:
            for perm in self.Rol.Permisos:
                if perm.Codigo == permission_code:
                    return True
                    
        # 3. Verificar Permisos Específicos
        for perm in self.PermisosEspecificos:
            if perm.Codigo == permission_code:
                return True
                
        return False
