-- Tabla Intermedia Usuario-Permisos (Permisos específicos adicionales al Rol)
CREATE TABLE UsuarioPermisos (
    PersonaId INT NOT NULL,
    PermisoId INT NOT NULL,
    PRIMARY KEY (PersonaId, PermisoId),
    FOREIGN KEY (PersonaId) REFERENCES Personas(Id),
    FOREIGN KEY (PermisoId) REFERENCES Permisos(Id)
);
