import pyodbc
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, 'backend', '.env'))

server = os.getenv('DB_HOST', 'localhost')
user = os.getenv('DB_USERNAME', 'sa')
password = os.getenv('DB_PASSWORD', 'TuPasswordSeguro123!')
conn_str = f'DRIVER={{SQL Server}};SERVER={server},1433;UID={user};PWD={password};DATABASE=sistema_inventario;TrustServerCertificate=yes;'

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    # Verificar si existe
    cursor.execute("SELECT Id FROM Personas WHERE Correo = ?", 'admin@siicsa.com')
    row = cursor.fetchone()
    
    hashed = generate_password_hash('AdminPassword123!')
    print(f"Hash generado: {hashed[:20]}...")
    
    if row:
        print("Usuario existe. Actualizando password...")
        cursor.execute("UPDATE Personas SET PasswordHash = ?, IntentosFallidos = 0, BloqueoHasta = NULL WHERE Id = ?", (hashed, row.Id))
    else:
        print("Creando usuario...")
        sql = """
        INSERT INTO Personas (Nombre, Apellido, Correo, PasswordHash, EsUsuarioSistema, Activo, Celular, IntentosFallidos, TwoFactorEnabled)
        VALUES (?, ?, ?, ?, 1, 1, '573001234567', 0, 0)
        """
        cursor.execute(sql, ('Administrador', 'Sistema', 'admin@siicsa.com', hashed))
    
    conn.commit()
    print("Usuario actualizado/creado con PyODBC.")
        
    conn.close()
except Exception as e:
    print(f"Error PyODBC: {e}")
