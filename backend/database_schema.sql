-- CREACIÓN DE TABLAS BASE (CATÁLOGOS GLOBALES) --

CREATE TABLE Departamentos (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100) NOT NULL
);

CREATE TABLE Ciudades (
    Id INT PRIMARY KEY IDENTITY(1,1),
    DepartamentoId INT FOREIGN KEY REFERENCES Departamentos(Id),
    Nombre NVARCHAR(100) NOT NULL
);

-- TABLAS DE CONFIGURACIÓN DE LISTAS (DROPDOWNS) --

CREATE TABLE EstadoEquipo (Id INT PRIMARY KEY IDENTITY(1,1), Nombre NVARCHAR(50), Activo BIT DEFAULT 1);
CREATE TABLE TipoEquipo (Id INT PRIMARY KEY IDENTITY(1,1), Nombre NVARCHAR(50), Activo BIT DEFAULT 1);
CREATE TABLE Fabricantes (Id INT PRIMARY KEY IDENTITY(1,1), Nombre NVARCHAR(50), Activo BIT DEFAULT 1);
CREATE TABLE Puertos (Id INT PRIMARY KEY IDENTITY(1,1), Nombre NVARCHAR(50), Activo BIT DEFAULT 1); -- Ej: USB, HDMI
CREATE TABLE SistemasOperativos (Id INT PRIMARY KEY IDENTITY(1,1), Nombre NVARCHAR(100), Activo BIT DEFAULT 1);
CREATE TABLE Ofimaticas (Id INT PRIMARY KEY IDENTITY(1,1), Nombre NVARCHAR(100), Activo BIT DEFAULT 1);
CREATE TABLE Antivirus (Id INT PRIMARY KEY IDENTITY(1,1), Nombre NVARCHAR(100), Activo BIT DEFAULT 1);

-- HARDWARE CATALOGS --
CREATE TABLE MarcaProcesador (Id INT PRIMARY KEY IDENTITY(1,1), Nombre NVARCHAR(50));
CREATE TABLE TipoProcesador (Id INT PRIMARY KEY IDENTITY(1,1), MarcaId INT FOREIGN KEY REFERENCES MarcaProcesador(Id), Nombre NVARCHAR(50)); -- Core i5
CREATE TABLE GeneracionProcesador (Id INT PRIMARY KEY IDENTITY(1,1), TipoId INT FOREIGN KEY REFERENCES TipoProcesador(Id), Nombre NVARCHAR(50)); -- 13va Gen

CREATE TABLE TipoRAM (Id INT PRIMARY KEY IDENTITY(1,1), Nombre NVARCHAR(50)); -- DDR4
CREATE TABLE CapacidadRAM (Id INT PRIMARY KEY IDENTITY(1,1), Capacidad NVARCHAR(50)); -- 8GB, 16GB
CREATE TABLE BusRAM (Id INT PRIMARY KEY IDENTITY(1,1), TipoId INT FOREIGN KEY REFERENCES TipoRAM(Id), Velocidad NVARCHAR(50)); -- 3200MHz

CREATE TABLE TipoAlmacenamiento (Id INT PRIMARY KEY IDENTITY(1,1), Nombre NVARCHAR(50)); -- SSD, M.2
CREATE TABLE CapacidadAlmacenamiento (Id INT PRIMARY KEY IDENTITY(1,1), Capacidad NVARCHAR(50)); -- 512GB, 1TB
CREATE TABLE ProtocoloAlmacenamiento (Id INT PRIMARY KEY IDENTITY(1,1), TipoId INT FOREIGN KEY REFERENCES TipoAlmacenamiento(Id), Nombre NVARCHAR(50)); -- NVMe, SATA
CREATE TABLE FactorFormaAlmacenamiento (Id INT PRIMARY KEY IDENTITY(1,1), TipoId INT FOREIGN KEY REFERENCES TipoAlmacenamiento(Id), Nombre NVARCHAR(50)); -- 2280, 2.5"

-- ESTRUCTURA EMPRESARIAL --

CREATE TABLE Empresas (
    Id INT PRIMARY KEY IDENTITY(1,1),
    NIT NVARCHAR(20) UNIQUE NOT NULL,
    RazonSocial NVARCHAR(150) NOT NULL,
    Direccion NVARCHAR(200),
    CiudadId INT FOREIGN KEY REFERENCES Ciudades(Id),
    Telefono NVARCHAR(20),
    EsCliente BIT DEFAULT 0, -- 0 = Mi Empresa, 1 = Cliente
    Activo BIT DEFAULT 1
);

CREATE TABLE Sedes (
    Id INT PRIMARY KEY IDENTITY(1,1),
    EmpresaId INT FOREIGN KEY REFERENCES Empresas(Id),
    NombreSede NVARCHAR(100) NOT NULL,
    Direccion NVARCHAR(200),
    CiudadId INT FOREIGN KEY REFERENCES Ciudades(Id),
    Telefono NVARCHAR(20),
    Activo BIT DEFAULT 1
);

CREATE TABLE Areas (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100),
    Activo BIT DEFAULT 1
);

CREATE TABLE Cargos (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100),
    Activo BIT DEFAULT 1
);

-- USUARIOS DEL SISTEMA Y CONTACTOS --

CREATE TABLE Personas (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100) NOT NULL,
    Apellido NVARCHAR(100) NOT NULL,
    Correo NVARCHAR(150) UNIQUE NOT NULL,
    Celular NVARCHAR(20) DEFAULT '57',
    SedeId INT FOREIGN KEY REFERENCES Sedes(Id),
    AreaId INT FOREIGN KEY REFERENCES Areas(Id),
    CargoId INT FOREIGN KEY REFERENCES Cargos(Id),
    
    -- Campos exclusivos para Login del sistema
    PasswordHash NVARCHAR(MAX) NULL, -- Solo si es usuario del sistema
    EsUsuarioSistema BIT DEFAULT 0,
    EsContactoCliente BIT DEFAULT 0,
    
    -- 2FA y Seguridad
    TwoFactorSecret NVARCHAR(100) NULL,
    TwoFactorEnabled BIT DEFAULT 0,
    IntentosFallidos INT DEFAULT 0,
    BloqueoHasta DATETIME NULL,
    UltimoLogin DATETIME NULL,
    
    Activo BIT DEFAULT 1
);

-- INVENTARIO (EL NÚCLEO) --

CREATE TABLE Equipos (
    Id INT PRIMARY KEY IDENTITY(1,1),
    CodigoEquipo NVARCHAR(50) UNIQUE NOT NULL, -- ABC-123
    EmpresaId INT FOREIGN KEY REFERENCES Empresas(Id), -- Dueño del equipo
    
    -- Usuario Asignado
    UsuarioAsignadoId INT FOREIGN KEY REFERENCES Personas(Id), -- Quién lo tiene
    
    -- Datos Básicos
    EstadoEquipoId INT FOREIGN KEY REFERENCES EstadoEquipo(Id),
    TipoEquipoId INT FOREIGN KEY REFERENCES TipoEquipo(Id),
    FabricanteId INT FOREIGN KEY REFERENCES Fabricantes(Id),
    Modelo NVARCHAR(100),
    Serial NVARCHAR(100),
    FotoSerialUrl NVARCHAR(500), -- URL o Path del archivo adjunto
    
    EsPropio BIT DEFAULT 1,
    ProveedorAlquiler NVARCHAR(100),
    CodigoAlquiler NVARCHAR(100),
    
    -- Datos Software
    SistemaOperativoId INT FOREIGN KEY REFERENCES SistemasOperativos(Id),
    LicenciaSO NVARCHAR(100),
    OfimaticaId INT FOREIGN KEY REFERENCES Ofimaticas(Id),
    NombreOfimatica NVARCHAR(100), -- Si es Libre
    LicenciaOfimatica NVARCHAR(100),
    AntivirusId INT FOREIGN KEY REFERENCES Antivirus(Id),
    
    EquipoPertenece NVARCHAR(20), -- 'GRUPO_TRABAJO' o 'DOMINIO'
    NombreEnRed NVARCHAR(100),
    UltimoMantenimiento DATETIME,
    
    FechaCreacion DATETIME DEFAULT GETDATE(),
    CreadoPorId INT -- ID del usuario que lo creó
);

-- DETALLES DE HARDWARE (Relación 1 a Muchos) --

CREATE TABLE EquipoProcesadores (
    Id INT PRIMARY KEY IDENTITY(1,1),
    EquipoId INT FOREIGN KEY REFERENCES Equipos(Id),
    GeneracionId INT FOREIGN KEY REFERENCES GeneracionProcesador(Id) -- La generación ya sabe el tipo y marca
);

CREATE TABLE EquipoRAM (
    Id INT PRIMARY KEY IDENTITY(1,1),
    EquipoId INT FOREIGN KEY REFERENCES Equipos(Id),
    CapacidadId INT FOREIGN KEY REFERENCES CapacidadRAM(Id),
    BusId INT FOREIGN KEY REFERENCES BusRAM(Id),
    SlotNumero INT -- Slot 1, Slot 2...
);

CREATE TABLE EquipoAlmacenamiento (
    Id INT PRIMARY KEY IDENTITY(1,1),
    EquipoId INT FOREIGN KEY REFERENCES Equipos(Id),
    ProtocoloId INT FOREIGN KEY REFERENCES ProtocoloAlmacenamiento(Id),
    FactorFormaId INT FOREIGN KEY REFERENCES FactorFormaAlmacenamiento(Id),
    CapacidadId INT FOREIGN KEY REFERENCES CapacidadAlmacenamiento(Id),
    SlotNumero INT
);

CREATE TABLE EquipoAplicaciones (
    Id INT PRIMARY KEY IDENTITY(1,1),
    EquipoId INT FOREIGN KEY REFERENCES Equipos(Id),
    NombreAplicacion NVARCHAR(150),
    Version NVARCHAR(50),
    FechaInstalacion DATETIME DEFAULT GETDATE()
);

CREATE TABLE EquipoAdjuntos (
    Id INT PRIMARY KEY IDENTITY(1,1),
    EquipoId INT FOREIGN KEY REFERENCES Equipos(Id),
    TipoArchivo NVARCHAR(20), -- PDF, IMG, DOC
    RutaArchivo NVARCHAR(500),
    FechaSubida DATETIME DEFAULT GETDATE()
);

-- AUDITORÍA (HISTORIAL DETALLADO) --

CREATE TABLE AuditoriaLogs (
    Id INT PRIMARY KEY IDENTITY(1,1),
    TablaAfectada NVARCHAR(50),      -- Ej: "Equipos", "Personas"
    RegistroId INT,                  -- ID del registro afectado
    Accion NVARCHAR(20),             -- CREAR, EDITAR, ELIMINAR, MANTENIMIENTO
    UsuarioId INT FOREIGN KEY REFERENCES Personas(Id), -- Quién hizo el cambio
    Fecha DATETIME DEFAULT GETDATE(),
    
    -- Guardamos el detalle del cambio en JSON o Texto plano detallado
    DetalleCambio NVARCHAR(MAX), 
    
    CampoAfectado NVARCHAR(100),     -- Opcional, si queremos ser muy específicos
    ValorAntes NVARCHAR(MAX),
    ValorDespues NVARCHAR(MAX)
);

-- INDICES PARA BÚSQUEDAS RÁPIDAS --
CREATE INDEX IDX_Equipos_Busqueda ON Equipos(CodigoEquipo, Serial, NombreEnRed);
CREATE INDEX IDX_Personas_Busqueda ON Personas(Nombre, Apellido, Correo, Celular);
CREATE INDEX IDX_Empresas_NIT ON Empresas(NIT);
