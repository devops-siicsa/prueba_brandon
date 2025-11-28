from app import create_app
from app.models.core_models import Empresa, Sede
import sys

app = create_app()

with app.app_context():
    companies = Empresa.query.all()
    print(f"Total Companies: {len(companies)}")
    for c in companies:
        print(f"COMP: ID={c.Id}, Name='{c.RazonSocial}', Active={c.Activo}, EsCliente={c.EsCliente}")

    sedes = Sede.query.all()
    print(f"Total Sedes: {len(sedes)}")
    for s in sedes:
        p = Empresa.query.get(s.EmpresaId)
        print(f"SEDE: ID={s.Id}, Name='{s.NombreSede}', Active={s.Activo}, ParentID={s.EmpresaId}")
        if p:
            print(f"   -> Parent: Name='{p.RazonSocial}', Active={p.Activo}, EsCliente={p.EsCliente}")
            should_show = s.Activo and p.Activo and (not p.EsCliente)
            print(f"   -> Should Show in UserForm? {should_show}")
        else:
            print("   -> Parent NOT FOUND")
