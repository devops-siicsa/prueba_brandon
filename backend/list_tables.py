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
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
    tables = cursor.fetchall()
    print("Tablas encontradas:")
    for t in tables:
        print(f"- {t.TABLE_SCHEMA}.{t.TABLE_NAME}")
    conn.close()
except Exception as e:
    print(f"Error: {e}")
