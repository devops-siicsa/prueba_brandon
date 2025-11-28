/* 1. Si existe, la borramos (¡Cuidado, se pierden los datos!) */
IF OBJECT_ID(N'[dbo].[Aplicaciones]', N'U') IS NOT NULL 
    DROP TABLE [dbo].[Aplicaciones];

/* 2. La creamos de nuevo */
CREATE TABLE [dbo].[Aplicaciones] (
    [Id] INT IDENTITY(1,1) PRIMARY KEY,
    [Nombre] NVARCHAR(100) NOT NULL,
    [Activo] BIT NOT NULL DEFAULT 1
);
