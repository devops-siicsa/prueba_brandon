-- Expandir campo TipoArchivo de 20 a 100 caracteres para soportar MIME types largos
-- como application/vnd.openxmlformats-officedocument.wordprocessingml.document

USE sistema_inventario;
GO

ALTER TABLE EquipoAdjuntos
ALTER COLUMN TipoArchivo VARCHAR(100);
GO

PRINT 'Campo TipoArchivo expandido a 100 caracteres';
