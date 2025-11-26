from app import create_app
from sqlalchemy import text
from app.extensions import db

app = create_app()
with app.app_context():
    try:
        print("--- INICIO DIAGNOSTICO ---")
        print("1. Test Conexión SQL Pura")
        db.session.execute(text("SELECT 1"))
        print("   -> OK")
        
        print("2. Test Tabla Personas (SQL Puro)")
        db.session.execute(text("SELECT TOP 1 * FROM Personas"))
        print("   -> OK")
        
        print("3. Test ORM Persona")
        from app.models.auth_models import Persona
        p = Persona.query.first()
        print(f"   -> OK: {p}")
        
    except Exception as e:
        print(f"--- ERROR DETECTADO ---")
        print(e)
