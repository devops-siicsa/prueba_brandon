-- Crear tablas para Configuración de RAM (Actualizado)

-- 1. Tipo de RAM (DDR3, DDR4, DDR5, etc.)
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[TipoRAM]') AND type in (N'U'))
BEGIN
    CREATE TABLE TipoRAM (
        Id INT IDENTITY(1,1) PRIMARY KEY,
        Nombre NVARCHAR(50) NOT NULL,
        Activo BIT DEFAULT 1
    );
END

-- 2. Capacidad de RAM (4GB, 8GB, 16GB, etc.) - Global
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[CapacidadRAM]') AND type in (N'U'))
BEGIN
    CREATE TABLE CapacidadRAM (
        Id INT IDENTITY(1,1) PRIMARY KEY,
        Capacidad NVARCHAR(50) NOT NULL, -- Nombre del campo actualizado
        Activo BIT DEFAULT 1
    );
END

-- 3. Velocidad de RAM (BusRAM) - Dependiente de Tipo
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[BusRAM]') AND type in (N'U'))
BEGIN
    CREATE TABLE BusRAM (
        Id INT IDENTITY(1,1) PRIMARY KEY,
        Velocidad NVARCHAR(50) NOT NULL, -- Nombre del campo actualizado
        TipoId INT NOT NULL, -- Nombre del campo actualizado
        Activo BIT DEFAULT 1,
        CONSTRAINT FK_BusRAM_TipoRAM FOREIGN KEY (TipoId) REFERENCES TipoRAM(Id)
    );
END
