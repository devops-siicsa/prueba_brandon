from .auth_models import Persona
from .core_models import (
    Departamento, Ciudad, Empresa, Sede, Area, Cargo,
    EstadoEquipo, TipoEquipo, Fabricante, Puerto, SistemaOperativo, Ofimatica, Antivirus
)
from .inventory_models import (
    MarcaProcesador, TipoProcesador, GeneracionProcesador,
    TipoRAM, CapacidadRAM, BusRAM,
    TipoAlmacenamiento, CapacidadAlmacenamiento, ProtocoloAlmacenamiento, FactorFormaAlmacenamiento,
    Equipo, EquipoProcesador, EquipoRAM, EquipoAlmacenamiento, EquipoAplicacion, EquipoAdjunto
)
from .audit_models import AuditoriaLog
