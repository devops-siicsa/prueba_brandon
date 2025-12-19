-- ================================================================
-- MIGRACIÓN: EquipoAplicaciones - De NombreAplicacion a AplicacionId
-- Fecha: 2025-12-17
-- Descripción: Cambia el esquema de almacenar nombres de aplicaciones
--              a usar foreign keys para relacionarse con la tabla Aplicaciones
-- ================================================================

USE sistema_inventario;

-- Paso 1: Agregar nueva columna AplicacionId (temporal)
ALTER TABLE EquipoAplicaciones 
ADD COLUMN AplicacionId INT NULL AFTER EquipoId;

-- Paso 2: Migrar datos existentes - mapear NombreAplicacion a AplicacionId
-- Intentar encontrar coincidencias por nombre (case-insensitive)
UPDATE EquipoAplicaciones ea
INNER JOIN Aplicaciones a ON LOWER(TRIM(ea.NombreAplicacion)) = LOWER(TRIM(a.Nombre))
SET ea.AplicacionId = a.Id;

-- Paso 3: Verificar cuántos registros NO se pudieron mapear
SELECT COUNT(*) as RegistrosNoMapeados 
FROM EquipoAplicaciones 
WHERE AplicacionId IS NULL;

-- Paso 4: Eliminar registros que no se pudieron mapear (limpieza)
DELETE FROM EquipoAplicaciones WHERE AplicacionId IS NULL;

-- Paso 5: Hacer la columna AplicacionId NOT NULL
ALTER TABLE EquipoAplicaciones 
MODIFY COLUMN AplicacionId INT NOT NULL;

-- Paso 6: Eliminar la columna antigua NombreAplicacion (limpieza - no dejar basura)
ALTER TABLE EquipoAplicaciones 
DROP COLUMN NombreAplicacion;

-- Paso 7: Agregar el foreign key constraint
ALTER TABLE EquipoAplicaciones
ADD CONSTRAINT FK_EquipoAplicaciones_Aplicaciones 
FOREIGN KEY (AplicacionId) REFERENCES Aplicaciones(Id) ON DELETE CASCADE;

-- Paso 8: Agregar índice para mejorar performance en búsquedas
CREATE INDEX IDX_EquipoAplicaciones_AplicacionId ON EquipoAplicaciones(AplicacionId);
CREATE INDEX IDX_EquipoAplicaciones_EquipoId ON EquipoAplicaciones(EquipoId);

-- ================================================================
-- VERIFICACIÓN POST-MIGRACIÓN
-- ================================================================

-- Verificar estructura de la tabla
DESCRIBE EquipoAplicaciones;

-- Verificar que exista el foreign key
SELECT 
    CONSTRAINT_NAME,
    TABLE_NAME,
    COLUMN_NAME,
    REFERENCED_TABLE_NAME,
    REFERENCED_COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'sistema_inventario' 
  AND TABLE_NAME = 'EquipoAplicaciones'
  AND REFERENCED_TABLE_NAME IS NOT NULL;

-- Verificar integridad de datos (todos los registros deben tener una aplicación válida)
SELECT 
    COUNT(*) as TotalRegistros,
    COUNT(DISTINCT ea.AplicacionId) as AplicacionesUnicas
FROM EquipoAplicaciones ea
INNER JOIN Aplicaciones a ON ea.AplicacionId = a.Id;

SELECT '✓ Migración completada exitosamente' as Estado;
