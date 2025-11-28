-- Script para asignar permiso catalogs:view a roles operativos
-- Necesario para que puedan ver los listados de hardware al crear/editar equipos

USE sistema_inventario;
GO

DECLARE @PermisoId INT;
DECLARE @RolId INT;

-- Obtener ID del permiso catalogs:view
SELECT @PermisoId = Id FROM Permisos WHERE Codigo = 'catalogs:view';

IF @PermisoId IS NOT NULL
BEGIN
    -- 1. SOPORTE TECNICO
    SELECT @RolId = Id FROM Roles WHERE Nombre = 'SOPORTE TECNICO';
    IF @RolId IS NOT NULL AND NOT EXISTS (SELECT 1 FROM RolPermisos WHERE RolId = @RolId AND PermisoId = @PermisoId)
    BEGIN
        INSERT INTO RolPermisos (RolId, PermisoId) VALUES (@RolId, @PermisoId);
        PRINT 'Permiso catalogs:view asignado a SOPORTE TECNICO';
    END

    -- 2. ADMINISTRADOR CLIENTE
    SELECT @RolId = Id FROM Roles WHERE Nombre = 'ADMINISTRADOR CLIENTE';
    IF @RolId IS NOT NULL AND NOT EXISTS (SELECT 1 FROM RolPermisos WHERE RolId = @RolId AND PermisoId = @PermisoId)
    BEGIN
        INSERT INTO RolPermisos (RolId, PermisoId) VALUES (@RolId, @PermisoId);
        PRINT 'Permiso catalogs:view asignado a ADMINISTRADOR CLIENTE';
    END

    -- 3. SOPORTE CLIENTE
    SELECT @RolId = Id FROM Roles WHERE Nombre = 'SOPORTE CLIENTE';
    IF @RolId IS NOT NULL AND NOT EXISTS (SELECT 1 FROM RolPermisos WHERE RolId = @RolId AND PermisoId = @PermisoId)
    BEGIN
        INSERT INTO RolPermisos (RolId, PermisoId) VALUES (@RolId, @PermisoId);
        PRINT 'Permiso catalogs:view asignado a SOPORTE CLIENTE';
    END
END
ELSE
BEGIN
    PRINT 'Error: El permiso catalogs:view no existe en la tabla Permisos.';
END
