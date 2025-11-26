import pyodbc
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, 'backend', '.env'))

server = os.getenv('DB_HOST', 'localhost')
user = os.getenv('DB_USERNAME', 'sa')
password = os.getenv('DB_PASSWORD', 'TuPasswordSeguro123!')
conn_str = f'DRIVER={{SQL Server}};SERVER={server},1433;UID={user};PWD={password};DATABASE=sistema_inventario;TrustServerCertificate=yes;'

try:
    conn = pyodbc.connect(conn_str, autocommit=True)
    cursor = conn.cursor()
    
    with open('backend/granular_permissions.sql', 'r') as f:
        sql_script = f.read()
        
    try:
        cursor.execute("SELECT TOP 1 * FROM UsuarioPermisos")
        print("Tabla UsuarioPermisos ya existe.")
    except:
        print("Creando tabla UsuarioPermisos...")
        commands = sql_script.split(';')
        for cmd in commands:
            if cmd.strip():
                try:
                    cursor.execute(cmd)
                    print(f"Ejecutado: {cmd[:30]}...")
                except Exception as e:
                    print(f"Error en cmd: {e}")
                    
    print("Migración Granular finalizada.")
    conn.close()
except Exception as e:
    print(f"Error crítico: {e}")
