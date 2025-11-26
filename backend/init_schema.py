import pyodbc
import os
from dotenv import load_dotenv
import re

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, 'backend', '.env'))

server = os.getenv('DB_HOST', 'localhost')
user = os.getenv('DB_USERNAME', 'sa')
password = os.getenv('DB_PASSWORD', 'TuPasswordSeguro123!')
conn_str = f'DRIVER={{SQL Server}};SERVER={server},1433;UID={user};PWD={password};DATABASE=sistema_inventario;TrustServerCertificate=yes;'

try:
    conn = pyodbc.connect(conn_str, autocommit=True)
    cursor = conn.cursor()
    
    with open('backend/database_schema.sql', 'r', encoding='utf-8') as f:
        sql_script = f.read()
        
    # Separar por GO o ; (aunque el script usa ;)
    # Mejor separar por bloques lógicos si es posible, o ejecutar todo si el driver lo soporta.
    # PyODBC a veces falla con scripts largos. Separaremos por ;
    
    statements = sql_script.split(';')
    for stmt in statements:
        if stmt.strip():
            try:
                cursor.execute(stmt)
            except Exception as e:
                print(f"Error en stmt: {stmt[:50]}... -> {e}")
                
    print("Esquema inicializado.")
    conn.close()
except Exception as e:
    print(f"Error crítico: {e}")
