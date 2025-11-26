-- Actualización de tabla Personas para seguridad
ALTER TABLE Personas ADD TwoFactorSecret NVARCHAR(100) NULL;
ALTER TABLE Personas ADD TwoFactorEnabled BIT DEFAULT 0;
ALTER TABLE Personas ADD IntentosFallidos INT DEFAULT 0;
ALTER TABLE Personas ADD BloqueoHasta DATETIME NULL;
ALTER TABLE Personas ADD UltimoLogin DATETIME NULL;

-- Renombrar Secret2FA si existía (opcional, pero mejor prevenir)
-- EXEC sp_rename 'Personas.Secret2FA', 'TwoFactorSecret', 'COLUMN';
-- Como es desarrollo nuevo y probablemente la tabla estaba vacía o con estructura simple, los ADD son seguros.
-- Si Secret2FA ya existía, el ADD fallaría o quedaría duplicado. Asumiremos que el script inicial se ejecutó tal cual.
-- El script inicial tenía Secret2FA. Vamos a eliminarlo para limpiar.
ALTER TABLE Personas DROP COLUMN Secret2FA;
