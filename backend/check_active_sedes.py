from app import create_app
from app.models.core_models import Empresa, Sede
from app.extensions import db

app = create_app()

with app.app_context():
    active_internal_companies = Empresa.query.filter_by(EsCliente=False, Activo=True).all()
    print(f"Active Internal Companies: {[c.RazonSocial for c in active_internal_companies]}")
    
    company_ids = [c.Id for c in active_internal_companies]
    active_sedes = Sede.query.filter(Sede.EmpresaId.in_(company_ids), Sede.Activo==True).all()
    print(f"Active Internal Sedes: {[s.NombreSede for s in active_sedes]}")
