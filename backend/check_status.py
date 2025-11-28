from app import create_app
from app.models.core_models import Empresa, Sede
from app.extensions import db

app = create_app()

with app.app_context():
    print("--- EMPRESAS ---")
    print(f"{'ID':<5} {'RAZON SOCIAL':<30} {'ES CLIENTE':<10} {'ACTIVO':<10}")
    empresas = Empresa.query.all()
    for e in empresas:
        print(f"{e.Id:<5} {e.RazonSocial:<30} {str(e.EsCliente):<10} {str(e.Activo):<10}")

    print("\n--- SEDES ---")
    print(f"{'ID':<5} {'NOMBRE':<30} {'EMPRESA ID':<10} {'ACTIVO':<10}")
    sedes = Sede.query.all()
    for s in sedes:
        print(f"{s.Id:<5} {s.NombreSede:<30} {s.EmpresaId:<10} {str(s.Activo):<10}")
