-- Script de Reparación para Tablas de RAM (Versión Final - Compatible HeidiSQL)
-- Este script maneja las dependencias de claves foráneas y usa subconsultas para evitar errores de variables.

-- 1. Eliminar tabla dependiente (EquipoRAM) si existe
IF OBJECT_ID(N'[dbo].[EquipoRAM]', N'U') IS NOT NULL DROP TABLE [dbo].[EquipoRAM];

-- 2. Eliminar tablas de catálogo en orden inverso
IF OBJECT_ID(N'[dbo].[BusRAM]', N'U') IS NOT NULL DROP TABLE [dbo].[BusRAM];
IF OBJECT_ID(N'[dbo].[VelocidadRAM]', N'U') IS NOT NULL DROP TABLE [dbo].[VelocidadRAM]; -- Limpieza de intentos anteriores
IF OBJECT_ID(N'[dbo].[CapacidadRAM]', N'U') IS NOT NULL DROP TABLE [dbo].[CapacidadRAM];
IF OBJECT_ID(N'[dbo].[TipoRAM]', N'U') IS NOT NULL DROP TABLE [dbo].[TipoRAM];

-- 3. Recrear Tablas de Catálogo
CREATE TABLE TipoRAM (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Nombre NVARCHAR(50) NOT NULL,
    Activo BIT DEFAULT 1
);

CREATE TABLE CapacidadRAM (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Capacidad NVARCHAR(50) NOT NULL,
    Activo BIT DEFAULT 1
);

CREATE TABLE BusRAM (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Velocidad NVARCHAR(50) NOT NULL,
    TipoId INT NOT NULL,
    Activo BIT DEFAULT 1,
    CONSTRAINT FK_BusRAM_TipoRAM FOREIGN KEY (TipoId) REFERENCES TipoRAM(Id)
);

-- 4. Recrear tabla dependiente (EquipoRAM) vacía
CREATE TABLE EquipoRAM (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    EquipoId INT, -- FK a Equipos (se asume existente o se puede omitir constraint por ahora)
    CapacidadId INT,
    BusId INT,
    SlotNumero INT,
    CONSTRAINT FK_EquipoRAM_CapacidadRAM FOREIGN KEY (CapacidadId) REFERENCES CapacidadRAM(Id),
    CONSTRAINT FK_EquipoRAM_BusRAM FOREIGN KEY (BusId) REFERENCES BusRAM(Id)
);

-- 5. Insertar datos iniciales de ejemplo (Usando subconsultas directas para evitar errores de variables)
INSERT INTO TipoRAM (Nombre) VALUES ('DDR3'), ('DDR4'), ('DDR5');
INSERT INTO CapacidadRAM (Capacidad) VALUES ('4GB'), ('8GB'), ('16GB'), ('32GB');

-- Velocidades DDR4
INSERT INTO BusRAM (Velocidad, TipoId) 
SELECT '2400MHz', Id FROM TipoRAM WHERE Nombre = 'DDR4'
UNION ALL
SELECT '2666MHz', Id FROM TipoRAM WHERE Nombre = 'DDR4'
UNION ALL
SELECT '3200MHz', Id FROM TipoRAM WHERE Nombre = 'DDR4';

-- Velocidades DDR5
INSERT INTO BusRAM (Velocidad, TipoId) 
SELECT '4800MHz', Id FROM TipoRAM WHERE Nombre = 'DDR5'
UNION ALL
SELECT '5200MHz', Id FROM TipoRAM WHERE Nombre = 'DDR5';
