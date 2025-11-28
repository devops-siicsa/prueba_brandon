-- Corregir tipo de empresa
-- El usuario reporta que sus empresas aparecen como Clientes.
-- Esto asignará todas las empresas actuales como "Internas" (EsCliente = 0).

USE sistema_inventario;
GO

UPDATE Empresas
SET EsCliente = 0;

PRINT 'Empresas actualizadas a tipo Interno (EsCliente = 0).';
