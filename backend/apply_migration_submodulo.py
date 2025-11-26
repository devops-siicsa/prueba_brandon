import pyodbc
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

server = os.getenv('DB_HOST', 'localhost')
user = os.getenv('DB_USERNAME', 'sa')
password = os.getenv('DB_PASSWORD', 'TuPasswordSeguro123!')
conn_str = f'DRIVER={{SQL Server}};SERVER={server},1433;UID={user};PWD={password};DATABASE=sistema_inventario;TrustServerCertificate=yes;'

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    with open('backend/add_submodulo.sql', 'r') as f:
        sql = f.read()
        cursor.execute(sql)
        
    conn.commit()
    print("Migración aplicada exitosamente.")
    conn.close()
except Exception as e:
    print(f"Error: {e}")
