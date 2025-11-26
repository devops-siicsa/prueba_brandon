-- Tabla de Roles
CREATE TABLE Roles (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(50) NOT NULL UNIQUE, -- Super Admin, Admin, Soporte, etc.
    Scope NVARCHAR(20) NOT NULL, -- GLOBAL, TENANT
    Descripcion NVARCHAR(200),
    Activo BIT DEFAULT 1
);

-- Tabla de Permisos (Granular)
CREATE TABLE Permisos (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Codigo NVARCHAR(100) NOT NULL UNIQUE, -- auth:login, inventory:create
    Descripcion NVARCHAR(200),
    Modulo NVARCHAR(50), -- Auth, Inventory, Clients
    Activo BIT DEFAULT 1
);

-- Tabla Intermedia Rol-Permisos
CREATE TABLE RolPermisos (
    RolId INT NOT NULL,
    PermisoId INT NOT NULL,
    PRIMARY KEY (RolId, PermisoId),
    FOREIGN KEY (RolId) REFERENCES Roles(Id),
    FOREIGN KEY (PermisoId) REFERENCES Permisos(Id)
);

-- Actualizar Personas con Rol
ALTER TABLE Personas ADD RolId INT NULL;
ALTER TABLE Personas ADD CONSTRAINT FK_Personas_Roles FOREIGN KEY (RolId) REFERENCES Roles(Id);
