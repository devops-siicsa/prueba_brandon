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
    cursor.execute("SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Personas'")
    columns = cursor.fetchall()
    print("Columnas en Personas:")
    for col in columns:
        print(f"- {col.COLUMN_NAME} ({col.DATA_TYPE})")
    conn.close()
except Exception as e:
    print(f"Error: {e}")
