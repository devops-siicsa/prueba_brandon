import pyodbc
import os
from dotenv import load_dotenv

# Cargar .env
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

server = os.getenv('DB_HOST', 'localhost')
port = os.getenv('DB_PORT', '1433')
user = os.getenv('DB_USERNAME', 'sa')
password = os.getenv('DB_PASSWORD', 'TuPasswordSeguro123!')
driver = 'SQL Server'

server_str = f"{server},{port}"
conn_str = f'DRIVER={{{driver}}};SERVER={server_str};UID={user};PWD={password};DATABASE=sistema_inventario;TrustServerCertificate=yes;'

try:
    conn = pyodbc.connect(conn_str, autocommit=True)
    cursor = conn.cursor()
    
    with open('backend/update_auth_schema.sql', 'r') as f:
        sql_script = f.read()
        
    # Ejecutar línea por línea para evitar errores de bloque
    for statement in sql_script.split(';'):
        if statement.strip():
            try:
                cursor.execute(statement)
                print(f"Ejecutado: {statement[:50]}...")
            except Exception as e:
                print(f"Advertencia al ejecutar: {e}")
                
    print("Esquema actualizado exitosamente.")
    conn.close()
except Exception as e:
    print(f"Error crítico: {e}")
