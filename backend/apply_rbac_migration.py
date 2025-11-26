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
    
    with open('backend/rbac_schema.sql', 'r') as f:
        sql_script = f.read()
        
    # Ejecutar por bloques (separados por ;)
    # Nota: IDENTITY(1,1) y CREATE TABLE suelen ir bien.
    # Si falla, puede ser por dependencias.
    
    # Primero verificar si ya existen para no fallar
    try:
        cursor.execute("SELECT TOP 1 * FROM Roles")
        print("Tablas RBAC ya parecen existir.")
    except:
        print("Creando tablas RBAC...")
        # Separar comandos
        commands = sql_script.split(';')
        for cmd in commands:
            if cmd.strip():
                try:
                    cursor.execute(cmd)
                    print(f"Ejecutado: {cmd[:30]}...")
                except Exception as e:
                    print(f"Error en cmd: {e}")
                    
    print("Migración RBAC finalizada.")
    conn.close()
except Exception as e:
    print(f"Error crítico: {e}")
