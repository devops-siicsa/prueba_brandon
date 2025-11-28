-- Script de Reparación para Tablas de Almacenamiento
-- Maneja dependencias y estructura correcta con campo Activo

-- 1. Eliminar tabla dependiente (EquipoAlmacenamiento) si existe
IF OBJECT_ID(N'[dbo].[EquipoAlmacenamiento]', N'U') IS NOT NULL DROP TABLE [dbo].[EquipoAlmacenamiento];

-- 2. Eliminar tablas de catálogo en orden inverso (hijas primero)
IF OBJECT_ID(N'[dbo].[ProtocoloAlmacenamiento]', N'U') IS NOT NULL DROP TABLE [dbo].[ProtocoloAlmacenamiento];
IF OBJECT_ID(N'[dbo].[FactorFormaAlmacenamiento]', N'U') IS NOT NULL DROP TABLE [dbo].[FactorFormaAlmacenamiento];
IF OBJECT_ID(N'[dbo].[CapacidadAlmacenamiento]', N'U') IS NOT NULL DROP TABLE [dbo].[CapacidadAlmacenamiento];
IF OBJECT_ID(N'[dbo].[TipoAlmacenamiento]', N'U') IS NOT NULL DROP TABLE [dbo].[TipoAlmacenamiento];

-- 3. Recrear Tablas de Catálogo
CREATE TABLE TipoAlmacenamiento (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Nombre NVARCHAR(50) NOT NULL,
    Activo BIT DEFAULT 1
);

CREATE TABLE CapacidadAlmacenamiento (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Capacidad NVARCHAR(50) NOT NULL,
    Activo BIT DEFAULT 1
);

CREATE TABLE ProtocoloAlmacenamiento (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    TipoId INT NOT NULL,
    Nombre NVARCHAR(50) NOT NULL,
    Activo BIT DEFAULT 1,
    CONSTRAINT FK_Protocolo_Tipo FOREIGN KEY (TipoId) REFERENCES TipoAlmacenamiento(Id)
);

CREATE TABLE FactorFormaAlmacenamiento (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    TipoId INT NOT NULL,
    Nombre NVARCHAR(50) NOT NULL,
    Activo BIT DEFAULT 1,
    CONSTRAINT FK_FactorForma_Tipo FOREIGN KEY (TipoId) REFERENCES TipoAlmacenamiento(Id)
);

-- 4. Recrear tabla dependiente (EquipoAlmacenamiento) vacía
-- Nota: Ajustar columnas según necesidad real del inventario, aquí pongo lo básico
CREATE TABLE EquipoAlmacenamiento (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    EquipoId INT, 
    TipoId INT,
    CapacidadId INT,
    ProtocoloId INT,
    FactorFormaId INT,
    CONSTRAINT FK_EquipoAlmacenamiento_Tipo FOREIGN KEY (TipoId) REFERENCES TipoAlmacenamiento(Id),
    CONSTRAINT FK_EquipoAlmacenamiento_Capacidad FOREIGN KEY (CapacidadId) REFERENCES CapacidadAlmacenamiento(Id),
    CONSTRAINT FK_EquipoAlmacenamiento_Protocolo FOREIGN KEY (ProtocoloId) REFERENCES ProtocoloAlmacenamiento(Id),
    CONSTRAINT FK_EquipoAlmacenamiento_FactorForma FOREIGN KEY (FactorFormaId) REFERENCES FactorFormaAlmacenamiento(Id)
);

-- 5. Insertar datos iniciales (Usando subconsultas para evitar variables)

-- Tipos
INSERT INTO TipoAlmacenamiento (Nombre) VALUES ('MECANICO'), ('SSD'), ('M.2');

-- Capacidades Globales
INSERT INTO CapacidadAlmacenamiento (Capacidad) VALUES 
('128GB'), ('240GB'), ('256GB'), ('480GB'), ('500GB'), ('512GB'), ('1TB'), ('2TB'), ('4TB');

-- Protocolos y Factores de Forma por Tipo

-- MECANICO
INSERT INTO ProtocoloAlmacenamiento (Nombre, TipoId)
SELECT 'SATA', Id FROM TipoAlmacenamiento WHERE Nombre = 'MECANICO';

INSERT INTO FactorFormaAlmacenamiento (Nombre, TipoId)
SELECT '3.5', Id FROM TipoAlmacenamiento WHERE Nombre = 'MECANICO'
UNION ALL
SELECT '2.5', Id FROM TipoAlmacenamiento WHERE Nombre = 'MECANICO';

-- SSD
INSERT INTO ProtocoloAlmacenamiento (Nombre, TipoId)
SELECT 'SATA', Id FROM TipoAlmacenamiento WHERE Nombre = 'SSD';

INSERT INTO FactorFormaAlmacenamiento (Nombre, TipoId)
SELECT '2.5', Id FROM TipoAlmacenamiento WHERE Nombre = 'SSD';

-- M.2
INSERT INTO ProtocoloAlmacenamiento (Nombre, TipoId)
SELECT 'SATA', Id FROM TipoAlmacenamiento WHERE Nombre = 'M.2'
UNION ALL
SELECT 'PCIe', Id FROM TipoAlmacenamiento WHERE Nombre = 'M.2'
UNION ALL
SELECT 'NVMe', Id FROM TipoAlmacenamiento WHERE Nombre = 'M.2'; -- Agrego NVMe comunmente asociado

INSERT INTO FactorFormaAlmacenamiento (Nombre, TipoId)
SELECT '2280', Id FROM TipoAlmacenamiento WHERE Nombre = 'M.2'
UNION ALL
SELECT '2242', Id FROM TipoAlmacenamiento WHERE Nombre = 'M.2'
UNION ALL
SELECT '2230', Id FROM TipoAlmacenamiento WHERE Nombre = 'M.2'
UNION ALL
SELECT '22110', Id FROM TipoAlmacenamiento WHERE Nombre = 'M.2';
