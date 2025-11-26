from app import create_app
from app.models.auth_models import Persona
from app.extensions import db

app = create_app()
with app.app_context():
    user = Persona.query.filter_by(Correo='admin@siicsa.com').first()
    if user:
        print(f"Usuario encontrado: {user.Nombre} {user.Apellido}")
        print(f"PasswordHash: {user.PasswordHash[:20]}..." if user.PasswordHash else "NO HASH")
        print(f"IntentosFallidos: {user.IntentosFallidos}")
        print(f"BloqueoHasta: {user.BloqueoHasta}")
        print(f"Activo: {user.Activo}")
    else:
        print("Usuario admin@siicsa.com NO encontrado.")
