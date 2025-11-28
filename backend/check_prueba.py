from app import create_app
from app.models.core_models import Empresa, Sede

app = create_app()

with app.app_context():
    # Find the problematic company
    comp = Empresa.query.filter(Empresa.RazonSocial.like('%Prueba%')).first()
    if comp:
        print(f"COMPANY: {comp.RazonSocial} | ID: {comp.Id} | Active: {comp.Activo} | EsCliente: {comp.EsCliente}")
        sedes = Sede.query.filter_by(EmpresaId=comp.Id).all()
        for s in sedes:
            print(f"  SEDE: {s.NombreSede} | ID: {s.Id} | Active: {s.Activo}")
            should_show = s.Activo and comp.Activo and (not comp.EsCliente)
            print(f"  -> Visible in UserForm? {should_show}")
    else:
        print("Company not found")
