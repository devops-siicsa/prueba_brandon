from app import create_app
from app.models.core_models import Empresa
from app.extensions import db

app = create_app()

with app.app_context():
    empresas = Empresa.query.all()
    print(f"Total Empresas: {len(empresas)}")
    print("-" * 60)
    print(f"{'ID':<5} {'RAZON SOCIAL':<40} {'ES CLIENTE':<10}")
    print("-" * 60)
    for e in empresas:
        print(f"{e.Id:<5} {e.RazonSocial:<40} {e.EsCliente:<10}")
