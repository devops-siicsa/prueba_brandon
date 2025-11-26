import pyodbc
import os
from dotenv import load_dotenv

# Cargar .env
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

server = os.getenv('DB_HOST', 'localhost')
port = os.getenv('DB_PORT', '1433')
user = os.getenv('DB_USERNAME', 'sa')
password = os.getenv('DB_PASSWORD', 'YourStrongPassword123')
driver = 'SQL Server'

# Intentar formato server,port
server_str = f"{server},{port}"

print(f"Conectando a: {server_str} con usuario {user} y driver {driver}")

# Connection string para master
conn_str = f'DRIVER={{{driver}}};SERVER={server_str};UID={user};PWD={password};DATABASE=master;TrustServerCertificate=yes;'

try:
    conn = pyodbc.connect(conn_str, autocommit=True)
    cursor = conn.cursor()
    
    cursor.execute("IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'sistema_inventario') BEGIN CREATE DATABASE sistema_inventario; END")
    print("Base de datos 'sistema_inventario' verificada/creada exitosamente.")
    
    conn.close()
except Exception as e:
    print(f"Error detallado: {e}")
