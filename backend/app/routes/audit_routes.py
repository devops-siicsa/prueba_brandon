from flask import Blueprint, jsonify, request
from app.models.audit_models import AuditoriaLog
from app.models.auth_models import Persona
from app.utils.decorators import token_required, requires_permission
from sqlalchemy import desc

audit_bp = Blueprint('audit', __name__, url_prefix='/api/audit')

@audit_bp.route('/logs', methods=['GET'])
@token_required
@requires_permission('audit:view_full')
def get_audit_logs(current_user):
    try:
        # Filtros
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        user_name = request.args.get('userName')
        user_doc = request.args.get('userDoc')
        company_name = request.args.get('companyName')
        company_nit = request.args.get('companyNit')

        # Fix: Define variables that were missing
        user_id = request.args.get('userId')
        action = request.args.get('action')
        table = request.args.get('table')
        date_from = request.args.get('dateFrom')
        date_to = request.args.get('dateTo')

        print(f"DEBUG AUDIT: Params received: {request.args}")

        query = AuditoriaLog.query

        if user_id:
            query = query.filter(AuditoriaLog.UsuarioId == user_id)
        if action:
            print(f"DEBUG AUDIT: Filtering by action: {action}")
            query = query.filter(AuditoriaLog.Accion == action)
        if table:
            query = query.filter(AuditoriaLog.TablaAfectada.ilike(f"%{table}%"))
        if date_from:
            query = query.filter(AuditoriaLog.Fecha >= date_from)
        if date_to:
            query = query.filter(AuditoriaLog.Fecha <= f"{date_to} 23:59:59")

        # Join con Persona, Sede y Empresa (Always)
        from app.models.core_models import Sede, Empresa
        query = query.outerjoin(Persona, AuditoriaLog.UsuarioId == Persona.Id)\
                     .outerjoin(Sede, Persona.SedeId == Sede.Id)\
                     .outerjoin(Empresa, Sede.EmpresaId == Empresa.Id)

        # Filtros avanzados
        if user_name:
            # Buscar en Nombre o Apellido
            query = query.filter(
                (Persona.Nombre.ilike(f"%{user_name}%")) | 
                (Persona.Apellido.ilike(f"%{user_name}%"))
            )
        
        if user_doc:
            query = query.filter(Persona.Documento.ilike(f"%{user_doc}%"))

        if company_name:
            query = query.filter(Empresa.RazonSocial.ilike(f"%{company_name}%"))
        if company_nit:
            query = query.filter(Empresa.NIT.ilike(f"%{company_nit}%"))
        
        # Selección de campos
        query = query.add_columns(
            AuditoriaLog.Id,
            AuditoriaLog.TablaAfectada,
            AuditoriaLog.Accion,
            AuditoriaLog.Fecha,
            AuditoriaLog.DetalleCambio,
            AuditoriaLog.CampoAfectado,
            AuditoriaLog.ValorAntes,
            AuditoriaLog.ValorDespues,
            Persona.Nombre.label('UsuarioNombre'),
            Persona.Apellido.label('UsuarioApellido'),
            Persona.Documento.label('UsuarioDocumento'),
            Empresa.RazonSocial.label('EmpresaNombre'),
            Empresa.NIT.label('EmpresaNIT'),
            Sede.NombreSede.label('SedeNombre')
        )

        # Ordenar por fecha descendente
        query = query.order_by(desc(AuditoriaLog.Fecha))

        # Paginación
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        
        logs = []
        for item in pagination.items:
            log_entry = {
                'Id': item.Id,
                'Tabla': item.TablaAfectada,
                'Accion': item.Accion,
                'Fecha': item.Fecha.isoformat(),
                'Usuario': f"{item.UsuarioNombre or ''} {item.UsuarioApellido or ''}".strip() or 'Sistema/Desconocido',
                'UsuarioDocumento': item.UsuarioDocumento,
                'Empresa': item.EmpresaNombre or '-',
                'EmpresaNIT': item.EmpresaNIT,
                'Sede': item.SedeNombre or '-',
                'Detalle': item.DetalleCambio,
                'Campo': item.CampoAfectado,
                'ValorAntes': item.ValorAntes,
                'ValorDespues': item.ValorDespues
            }
            logs.append(log_entry)

        print(f"DEBUG AUDIT: Returning {len(logs)} logs (Total: {pagination.total})")

        return jsonify({
            'logs': logs,
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': page
        }), 200

    except Exception as e:
        print(f"Error fetching audit logs: {e}")
        return jsonify({'message': 'Error al obtener logs de auditoría'}), 500

@audit_bp.route('/filters', methods=['GET'])
@token_required
def get_audit_filters(current_user):
    try:
        from app.models.core_models import Sede, Empresa
        from app.extensions import db
        
        # 1. Tablas (Distinct from AuditoriaLog)
        tables = [r[0] for r in db.session.query(AuditoriaLog.TablaAfectada).distinct().all() if r[0]]
        
        # 2. Usuarios (Solo los que tienen logs)
        # Join Persona con AuditoriaLog
        users_query = db.session.query(Persona.Nombre, Persona.Apellido, Persona.Documento)\
            .join(AuditoriaLog, Persona.Id == AuditoriaLog.UsuarioId)\
            .distinct().all()
            
        users = []
        user_docs = []
        for u in users_query:
            full_name = f"{u.Nombre} {u.Apellido}".strip()
            if full_name not in users:
                users.append(full_name)
            if u.Documento and u.Documento not in user_docs:
                user_docs.append(u.Documento)
                
        # 3. Empresas (Solo las que tienen usuarios con logs)
        # Join Empresa -> Sede -> Persona -> AuditoriaLog
        companies_query = db.session.query(Empresa.RazonSocial, Empresa.NIT)\
            .join(Sede, Empresa.Id == Sede.EmpresaId)\
            .join(Persona, Sede.Id == Persona.SedeId)\
            .join(AuditoriaLog, Persona.Id == AuditoriaLog.UsuarioId)\
            .distinct().all()
            
        companies = [c.RazonSocial for c in companies_query if c.RazonSocial]
        company_nits = [c.NIT for c in companies_query if c.NIT]
        
        return jsonify({
            'tables': sorted(tables),
            'users': sorted(users),
            'user_docs': sorted(user_docs),
            'companies': sorted(companies),
            'company_nits': sorted(company_nits)
        })
    except Exception as e:
        print(f"Error fetching audit filters: {e}")
        return jsonify({'message': 'Error al obtener filtros'}), 500
