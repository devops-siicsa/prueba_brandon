from app import create_app
from app.models import Persona, Empresa, Equipo

app = create_app()

with app.app_context():
    print("Modelos importados correctamente:")
    print(f"- Persona: {Persona.__tablename__}")
    print(f"- Empresa: {Empresa.__tablename__}")
    print(f"- Equipo: {Equipo.__tablename__}")
