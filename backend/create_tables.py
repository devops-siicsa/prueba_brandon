from app import create_app
from app.extensions import db
# Importar modelos para asegurar que SQLAlchemy los conozca
from app.models.core_models import Aplicacion

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        print("Creando tablas...")
        db.create_all()
        print("Tablas creadas/verificadas exitosamente.")
