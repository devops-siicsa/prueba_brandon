-- Migration: Add NombreOriginal column to EquipoAdjuntos
-- This stores the original filename separately from the Azure URL
-- Allows clean retrieval without fragile string parsing

USE sistema_inventario;

-- Add the new column
ALTER TABLE EquipoAdjuntos
ADD NombreOriginal VARCHAR(255);

-- Optional: Backfill existing records by extracting from URL
-- This attempts to extract filename from Azure blob URLs
-- Format: https://.../equipos/2/uuid_filename.ext?sas
UPDATE EquipoAdjuntos
SET NombreOriginal = SUBSTRING(
    RutaArchivo,
    CHARINDEX('_', REVERSE(SUBSTRING(RutaArchivo, 1, CHARINDEX('?', RutaArchivo + '?') - 1))) + 1,
    CHARINDEX('?', RutaArchivo + '?') - CHARINDEX('_', REVERSE(SUBSTRING(RutaArchivo, 1, CHARINDEX('?', RutaArchivo + '?') - 1))) - 1
)
WHERE RutaArchivo IS NOT NULL 
  AND RutaArchivo LIKE '%blob.core.windows.net%'
  AND NombreOriginal IS NULL;

PRINT 'Migration completed: NombreOriginal column added and backfilled';
