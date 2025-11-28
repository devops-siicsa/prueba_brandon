from app import create_app
from app.models.core_models import Empresa, Sede

app = create_app()

with app.app_context():
    print("-" * 80)
    print(f"{'ID':<5} {'TYPE':<10} {'NAME':<30} {'ACTIVE':<10} {'CLIENT?':<10} {'PARENT':<10}")
    print("-" * 80)
    
    # Check Companies
    companies = Empresa.query.all()
    for c in companies:
        print(f"{c.Id:<5} {'COMPANY':<10} {c.RazonSocial[:30]:<30} {str(c.Activo):<10} {str(c.EsCliente):<10} {'-':<10}")

    print("-" * 80)

    # Check Sedes
    sedes = Sede.query.all()
    for s in sedes:
        parent = Empresa.query.get(s.EmpresaId)
        parent_name = parent.RazonSocial if parent else "UNKNOWN"
        parent_active = str(parent.Activo) if parent else "?"
        parent_client = str(parent.EsCliente) if parent else "?"
        
        print(f"{s.Id:<5} {'SEDE':<10} {s.NombreSede[:30]:<30} {str(s.Activo):<10} {'-':<10} {s.EmpresaId} ({parent_name})")
        print(f"    -> Filter Logic: SedeActive={s.Activo}, ParentActive={parent_active}, ParentNotClient={not parent.EsCliente if parent else '?'}")
        
    print("-" * 80)
