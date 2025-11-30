from app import create_app
from app.extensions import db

app = create_app()
with app.app_context():
    try:
        print("Intentando crear tablas...")
        db.create_all()
        print("Tablas creadas exitosamente.")
    except Exception as e:
        print(f"Error creando tablas: {e}")
        import traceback
        traceback.print_exc()
