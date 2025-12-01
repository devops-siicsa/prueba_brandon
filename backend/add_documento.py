from app import create_app, db
from sqlalchemy import text

app = create_app()

with app.app_context():
    try:
        print("Agregando columna Documento a Personas...")
        with db.engine.connect() as conn:
            conn.execute(text("ALTER TABLE Personas ADD Documento NVARCHAR(20) NULL"))
            conn.commit()
        print("Columna agregada exitosamente.")
    except Exception as e:
        print(f"Error (puede que ya exista): {e}")
