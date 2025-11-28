from app import create_app
from app.models.core_models import Empresa, Sede

app = create_app()

with app.app_context():
    # Find the problematic sede
    sede = Sede.query.filter(Sede.NombreSede.like('%CHIPICHAPE%')).first()
    if sede:
        comp = Empresa.query.get(sede.EmpresaId)
        print(f"SEDE: {sede.NombreSede} | ID: {sede.Id} | Active: {sede.Activo}")
        if comp:
            print(f"  -> PARENT: {comp.RazonSocial} | ID: {comp.Id} | Active: {comp.Activo} | EsCliente: {comp.EsCliente}")
            should_show = sede.Activo and comp.Activo and (not comp.EsCliente)
            print(f"  -> Visible in UserForm? {should_show}")
            print(f"  -> Logic: {sede.Activo} AND {comp.Activo} AND (NOT {comp.EsCliente})")
        else:
            print("  -> PARENT NOT FOUND")
    else:
        print("Sede not found")
