from app import create_app, db
from app.models.audit_models import AuditoriaLog

app = create_app()

with app.app_context():
    count = AuditoriaLog.query.count()
    print(f"Total Audit Logs: {count}")
    
    if count > 0:
        last = AuditoriaLog.query.order_by(AuditoriaLog.Fecha.desc()).first()
        print(f"Last Log: {last.Accion} on {last.TablaAfectada} at {last.Fecha}")
