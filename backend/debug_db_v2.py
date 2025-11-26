import pyodbc
import os
from dotenv import load_dotenv

# Cargar .env correctamente
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, 'backend', '.env'))

print("--- PYODBC TEST ---")
try:
    server = os.getenv('DB_HOST', 'localhost')
    user = os.getenv('DB_USERNAME', 'sa')
    password = os.getenv('DB_PASSWORD', 'TuPasswordSeguro123!')
    # Forzamos driver SQL Server
    conn_str = f'DRIVER={{SQL Server}};SERVER={server},1433;UID={user};PWD={password};DATABASE=sistema_inventario;TrustServerCertificate=yes;'
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Conectado. Consultando Personas...")
    cursor.execute("SELECT TOP 1 * FROM Personas")
    row = cursor.fetchone()
    print(f"Row: {row}")
    conn.close()
    print("PYODBC OK")
except Exception as e:
    print(f"PYODBC ERROR: {e}")

print("\n--- SQLALCHEMY TEST ---")
try:
    from app import create_app
    from sqlalchemy import text
    from app.extensions import db
    app = create_app()
    with app.app_context():
        print("Intentando SELECT 1 con SQLAlchemy...")
        db.session.execute(text("SELECT 1"))
        print("SQLAlchemy SELECT 1 OK")
except Exception as e:
    print(f"SQLAlchemy ERROR: {e}")
