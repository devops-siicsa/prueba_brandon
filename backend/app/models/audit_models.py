from app.extensions import db
from datetime import datetime

class AuditoriaLog(db.Model):
    __tablename__ = 'AuditoriaLogs'
    
    Id = db.Column(db.Integer, primary_key=True)
    TablaAfectada = db.Column(db.String(50))
    RegistroId = db.Column(db.Integer)
    Accion = db.Column(db.String(20)) # CREAR, EDITAR, ELIMINAR
    UsuarioId = db.Column(db.Integer, db.ForeignKey('Personas.Id'))
    Fecha = db.Column(db.DateTime, default=datetime.now)
    
    DetalleCambio = db.Column(db.String(None)) # NVARCHAR(MAX)
    CampoAfectado = db.Column(db.String(100))
    ValorAntes = db.Column(db.String(None))
    ValorDespues = db.Column(db.String(None))
