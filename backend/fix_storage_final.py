from app import create_app, db
from sqlalchemy import text

app = create_app()

def run_fix():
    with app.app_context():
        print("Iniciando creación manual de tablas de almacenamiento...")
        try:
            with db.engine.connect() as conn:
                # 1. Limpieza (DROP)
                print("Limpiando tablas antiguas...")
                drops = [
                    "IF OBJECT_ID(N'[dbo].[EquipoAlmacenamiento]', N'U') IS NOT NULL DROP TABLE [dbo].[EquipoAlmacenamiento]",
                    "IF OBJECT_ID(N'[dbo].[ProtocoloAlmacenamiento]', N'U') IS NOT NULL DROP TABLE [dbo].[ProtocoloAlmacenamiento]",
                    "IF OBJECT_ID(N'[dbo].[FactorFormaAlmacenamiento]', N'U') IS NOT NULL DROP TABLE [dbo].[FactorFormaAlmacenamiento]",
                    "IF OBJECT_ID(N'[dbo].[CapacidadAlmacenamiento]', N'U') IS NOT NULL DROP TABLE [dbo].[CapacidadAlmacenamiento]",
                    "IF OBJECT_ID(N'[dbo].[TipoAlmacenamiento]', N'U') IS NOT NULL DROP TABLE [dbo].[TipoAlmacenamiento]"
                ]
                for stmt in drops:
                    conn.execute(text(stmt))
                conn.commit()

                # 2. Creación (CREATE)
                print("Creando tablas...")
                creates = [
                    """CREATE TABLE TipoAlmacenamiento (
                        Id INT IDENTITY(1,1) PRIMARY KEY,
                        Nombre NVARCHAR(50) NOT NULL,
                        Activo BIT DEFAULT 1
                    )""",
                    """CREATE TABLE CapacidadAlmacenamiento (
                        Id INT IDENTITY(1,1) PRIMARY KEY,
                        Capacidad NVARCHAR(50) NOT NULL,
                        Activo BIT DEFAULT 1
                    )""",
                    """CREATE TABLE ProtocoloAlmacenamiento (
                        Id INT IDENTITY(1,1) PRIMARY KEY,
                        TipoId INT NOT NULL,
                        Nombre NVARCHAR(50) NOT NULL,
                        Activo BIT DEFAULT 1,
                        CONSTRAINT FK_Protocolo_Tipo FOREIGN KEY (TipoId) REFERENCES TipoAlmacenamiento(Id)
                    )""",
                    """CREATE TABLE FactorFormaAlmacenamiento (
                        Id INT IDENTITY(1,1) PRIMARY KEY,
                        TipoId INT NOT NULL,
                        Nombre NVARCHAR(50) NOT NULL,
                        Activo BIT DEFAULT 1,
                        CONSTRAINT FK_FactorForma_Tipo FOREIGN KEY (TipoId) REFERENCES TipoAlmacenamiento(Id)
                    )""",
                    """CREATE TABLE EquipoAlmacenamiento (
                        Id INT IDENTITY(1,1) PRIMARY KEY,
                        EquipoId INT, 
                        TipoId INT,
                        CapacidadId INT,
                        ProtocoloId INT,
                        FactorFormaId INT,
                        SlotNumero INT,
                        CONSTRAINT FK_EquipoAlmacenamiento_Tipo FOREIGN KEY (TipoId) REFERENCES TipoAlmacenamiento(Id),
                        CONSTRAINT FK_EquipoAlmacenamiento_Capacidad FOREIGN KEY (CapacidadId) REFERENCES CapacidadAlmacenamiento(Id),
                        CONSTRAINT FK_EquipoAlmacenamiento_Protocolo FOREIGN KEY (ProtocoloId) REFERENCES ProtocoloAlmacenamiento(Id),
                        CONSTRAINT FK_EquipoAlmacenamiento_FactorForma FOREIGN KEY (FactorFormaId) REFERENCES FactorFormaAlmacenamiento(Id)
                    )"""
                ]
                for stmt in creates:
                    conn.execute(text(stmt))
                conn.commit()
                print("Tablas creadas.")

                # 3. Datos Iniciales (INSERT)
                print("Insertando datos...")
                inserts = [
                    "INSERT INTO TipoAlmacenamiento (Nombre) VALUES ('MECANICO'), ('SSD'), ('M.2')",
                    "INSERT INTO CapacidadAlmacenamiento (Capacidad) VALUES ('128GB'), ('240GB'), ('256GB'), ('480GB'), ('500GB'), ('512GB'), ('1TB'), ('2TB'), ('4TB')",
                    
                    # Protocolos
                    "INSERT INTO ProtocoloAlmacenamiento (Nombre, TipoId) SELECT 'SATA', Id FROM TipoAlmacenamiento WHERE Nombre = 'MECANICO'",
                    "INSERT INTO ProtocoloAlmacenamiento (Nombre, TipoId) SELECT 'SATA', Id FROM TipoAlmacenamiento WHERE Nombre = 'SSD'",
                    "INSERT INTO ProtocoloAlmacenamiento (Nombre, TipoId) SELECT 'SATA', Id FROM TipoAlmacenamiento WHERE Nombre = 'M.2'",
                    "INSERT INTO ProtocoloAlmacenamiento (Nombre, TipoId) SELECT 'PCIe', Id FROM TipoAlmacenamiento WHERE Nombre = 'M.2'",
                    "INSERT INTO ProtocoloAlmacenamiento (Nombre, TipoId) SELECT 'NVMe', Id FROM TipoAlmacenamiento WHERE Nombre = 'M.2'",
                    
                    # Factores de Forma
                    "INSERT INTO FactorFormaAlmacenamiento (Nombre, TipoId) SELECT '3.5', Id FROM TipoAlmacenamiento WHERE Nombre = 'MECANICO'",
                    "INSERT INTO FactorFormaAlmacenamiento (Nombre, TipoId) SELECT '2.5', Id FROM TipoAlmacenamiento WHERE Nombre = 'MECANICO'",
                    "INSERT INTO FactorFormaAlmacenamiento (Nombre, TipoId) SELECT '2.5', Id FROM TipoAlmacenamiento WHERE Nombre = 'SSD'",
                    "INSERT INTO FactorFormaAlmacenamiento (Nombre, TipoId) SELECT '2280', Id FROM TipoAlmacenamiento WHERE Nombre = 'M.2'",
                    "INSERT INTO FactorFormaAlmacenamiento (Nombre, TipoId) SELECT '2242', Id FROM TipoAlmacenamiento WHERE Nombre = 'M.2'",
                    "INSERT INTO FactorFormaAlmacenamiento (Nombre, TipoId) SELECT '2230', Id FROM TipoAlmacenamiento WHERE Nombre = 'M.2'",
                    "INSERT INTO FactorFormaAlmacenamiento (Nombre, TipoId) SELECT '22110', Id FROM TipoAlmacenamiento WHERE Nombre = 'M.2'"
                ]
                for stmt in inserts:
                    conn.execute(text(stmt))
                conn.commit()
                print("Datos insertados.")
            
        except Exception as e:
            print(f"ERROR CRÍTICO: {e}")

if __name__ == '__main__':
    run_fix()
