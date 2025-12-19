import pyodbc
import os
from dotenv import load_dotenv

# Carga el archivo .env una vez al inicio del archivo
load_dotenv()


# Función que devuelve la conexión a la base de datos
def get_db_connection():
    conn_str = (
        f"Driver={os.getenv('SQL_DRIVER')};"
        f"Server={os.getenv('SQL_SERVER')};"
        f"Database={os.getenv('SQL_DATABASE')};"
        f"Uid={os.getenv('SQL_USERNAME')};"
        f"Pwd={os.getenv('SQL_PASSWORD')};"
        "Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    )
    

    # Conexión a la base de datos
    conn = pyodbc.connect(conn_str, autocommit=True)
    return conn
