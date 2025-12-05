import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '..', '.env'))

class Config:
    # Construir URI de conexión
    _db_user = os.getenv('DB_USERNAME', 'sa')
    _db_pass = os.getenv('DB_PASSWORD', 'YourStrongPassword123')
    _db_host = os.getenv('DB_HOST', 'localhost')
    _db_port = os.getenv('DB_PORT', '1433')
    _db_name = os.getenv('DB_NAME', 'sistema_inventario')
    
    # Driver: Usamos ODBC Driver 18 for SQL Server
    _db_driver = os.getenv('DB_DRIVER', 'ODBC Driver 18 for SQL Server')
    
    # URI para SQLAlchemy
    # Nota: Para SQL Server, el formato host:port a veces requiere host,port o solo host si es default.
    # Usaremos host:port estándar.
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{_db_user}:{_db_pass}@{_db_host}:{_db_port}/{_db_name}?driver={_db_driver}&TrustServerCertificate=yes"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev_key')

    # CORS Configuration
    @staticmethod
    def get_cors_origins():
        origins_str = os.getenv('CORS_ORIGINS', 'http://localhost:3000')
        origins = []
        for origin in origins_str.split(','):
            origin = origin.strip()
            if origin.startswith('regex:'):
                import re
                origins.append(re.compile(origin[6:]))
            else:
                origins.append(origin)
        return origins

    CORS_ORIGINS = get_cors_origins()