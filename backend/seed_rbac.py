from app import create_app
from app.models.auth_models import Rol, Permiso, Persona
from app.extensions import db

app = create_app()

ROLES_DEF = [
    {'Nombre': 'SUPER ADMINISTRADOR', 'Scope': 'GLOBAL', 'Descripcion': 'Control total'},
    {'Nombre': 'ADMINISTRADOR', 'Scope': 'GLOBAL', 'Descripcion': 'Operativo interno'},
    {'Nombre': 'SOPORTE TECNICO', 'Scope': 'GLOBAL', 'Descripcion': 'Soporte interno'},
    {'Nombre': 'ADMINISTRADOR CLIENTE', 'Scope': 'TENANT', 'Descripcion': 'Gerente cliente'},
    {'Nombre': 'SOPORTE CLIENTE', 'Scope': 'TENANT', 'Descripcion': 'Consulta cliente'},
    {'Nombre': 'AUDITOR INTERNO', 'Scope': 'GLOBAL', 'Descripcion': 'Auditoría SIICSA'},
    {'Nombre': 'AUDITOR EXTERNO', 'Scope': 'TENANT', 'Descripcion': 'Auditoría Cliente'}
]

PERMISOS_DEF = [
    # Seguridad y Acceso (Antes Login)
    ('auth:login', 'Acceso al Sistema (Login)', 'Seguridad y Acceso', None),
    ('auth:2fa_bypass', 'Bypass 2FA (Recuperación)', 'Seguridad y Acceso', None),
    ('auth:2fa_required', 'Forzar 2FA', 'Seguridad y Acceso', None),
    
    # Navegación / Menú Principal
    ('menu:view_sys_config', 'Ver Configuración del Sistema', 'Navegación / Menú Principal', None),
    ('menu:view_client_config', 'Ver Configuración Cliente', 'Navegación / Menú Principal', None),
    
    # Panel: Configuración del Sistema
    ('sys_company:manage', 'Gestionar Empresas y Sedes Propias', 'Panel: Configuración del Sistema', None),
    ('sys_company:view', 'Ver Empresas Propias', 'Panel: Configuración del Sistema', None),
    ('sys_users:manage_all', 'Gestionar Usuarios Internos y Roles', 'Panel: Configuración del Sistema', None),
    ('sys_users:view_all', 'Ver Usuarios Internos', 'Panel: Configuración del Sistema', None),
    ('catalogs:create', 'Crear Catálogos (CPU, RAM, etc.)', 'Panel: Configuración del Sistema', None),
    ('catalogs:edit', 'Editar/Activar Opciones de Catálogos', 'Panel: Configuración del Sistema', None),
    ('catalogs:view', 'Ver Catálogos', 'Panel: Configuración del Sistema', None),
    ('catalogs:view_hidden', 'Ver Catálogos Ocultos', 'Panel: Configuración del Sistema', None),
    ('audit:view_full', 'Ver Log de Auditoría Completo', 'Panel: Configuración del Sistema', None),
    ('audit:export', 'Exportar Logs', 'Panel: Configuración del Sistema', None),
    
    # Panel: Configuración Cliente
    ('clients:create', 'Crear Nuevos Clientes', 'Panel: Configuración Cliente', None),
    ('clients:edit', 'Editar Datos de Clientes', 'Panel: Configuración Cliente', None),
    ('clients:manage_contacts', 'Gestionar Contactos de Clientes', 'Panel: Configuración Cliente', None),
    ('clients:view_list', 'Ver Lista Clientes', 'Panel: Configuración Cliente', None),
    ('clients:view_details', 'Ver Detalle Cliente', 'Panel: Configuración Cliente', None),
    ('clients:view_self', 'Ver Propia Empresa (Tenant)', 'Panel: Configuración Cliente', None),
    ('clients:edit_self_sedes', 'Editar Propias Sedes (Tenant)', 'Panel: Configuración Cliente', None),
    ('clients:manage_self_contacts', 'Gestionar Mis Contactos', 'Panel: Configuración Cliente', None),
    ('clients:view_contacts', 'Ver Contactos', 'Panel: Configuración Cliente', None),
    
    # Inventario y Dashboard (Agrupados)
    ('dashboard:view_all', 'Ver Dashboard Global (Todos)', 'Inventario y Dashboard', None),
    ('dashboard:view_self', 'Dashboard Propio', 'Inventario y Dashboard', None),
    ('dashboard:view_stats', 'Ver Estadísticas', 'Inventario y Dashboard', None),
    ('inventory:view_global', 'Ver Inventario Global', 'Inventario y Dashboard', None),
    ('inventory:view_self', 'Ver Inventario Propio', 'Inventario y Dashboard', None),
    ('inventory:create', 'Crear Equipos', 'Inventario y Dashboard', None),
    ('inventory:export', 'Exportar Reportes (Excel/PDF)', 'Inventario y Dashboard', None),
    ('inventory:export_bulk', 'Exportación Masiva (Auditor)', 'Inventario y Dashboard', None),
    
    # Ficha de Equipo (Detalle)
    ('equipment:edit_all', 'Edición Total', 'Ficha de Equipo (Detalle)', None),
    ('equipment:edit_sensitive', 'Editar Campos Sensibles', 'Ficha de Equipo (Detalle)', None),
    ('equipment:edit_hardware', 'Editar Hardware', 'Ficha de Equipo (Detalle)', None),
    ('equipment:edit_software', 'Editar Software', 'Ficha de Equipo (Detalle)', None),
    ('equipment:edit_user', 'Reasignar Usuario', 'Ficha de Equipo (Detalle)', None),
    ('equipment:view_sensitive', 'Ver Datos Sensibles', 'Ficha de Equipo (Detalle)', None),
    ('history:view_hidden', 'Ver Logs de Sistema Interno', 'Ficha de Equipo (Detalle)', None),
    ('history:view_full', 'Ver Historial Completo', 'Ficha de Equipo (Detalle)', None),
    ('history:view', 'Ver Historial', 'Ficha de Equipo (Detalle)', None),
    ('history:view_tenant', 'Ver Historial Tenant', 'Ficha de Equipo (Detalle)', None),
    ('history:comment', 'Comentar Historial', 'Ficha de Equipo (Detalle)', None),
    ('attachments:upload', 'Subir Adjuntos', 'Ficha de Equipo (Detalle)', None),
    ('attachments:view_all', 'Ver Todos Adjuntos', 'Ficha de Equipo (Detalle)', None),
    ('attachments:view', 'Ver Adjuntos', 'Ficha de Equipo (Detalle)', None),
    ('attachments:download', 'Descargar Adjuntos', 'Ficha de Equipo (Detalle)', None),
    ('maintenance:create', 'Registrar Mantenimiento', 'Ficha de Equipo (Detalle)', None),
    ('maintenance:log', 'Ver Logs Mantenimiento', 'Ficha de Equipo (Detalle)', None),
]

# Mapeo Rol -> Permisos (Simplificado para ejemplo, idealmente leer del MD parseado)
ROLE_PERMISSIONS = {
    'SUPER ADMINISTRADOR': [p[0] for p in PERMISOS_DEF], # Todo
    
    'ADMINISTRADOR': [
        'auth:login',
        # Menú
        'menu:view_sys_config', # Para ver catálogos
        'menu:view_client_config',
        # Config Sistema
        'catalogs:view',
        # Config Cliente
        'clients:create', 'clients:edit', 'clients:manage_contacts',
        'clients:view_list', 'clients:view_details', 'clients:view_contacts', # Implícitos para operar
        # Dashboard
        'dashboard:view_all', 'dashboard:view_stats',
        # Inventario
        'inventory:view_global', 'inventory:create', 'inventory:export',
        # Equipo
        'equipment:edit_all', # Incluye hardware, software, etc.
        'maintenance:log',
        'history:view', 'history:view_full', 'attachments:view_all', 'attachments:download' # Acceso lectura ficha
    ],

    'SOPORTE TECNICO': [
        'auth:login',
        # Menú (Ocultos Config)
        # Dashboard
        'dashboard:view_all',
        # Inventario
        'inventory:view_global', 'inventory:create',
        # Catálogos (Necesario para crear equipos)
        'catalogs:view',
        # Equipo (Operativo)
        'equipment:edit_hardware',
        'equipment:edit_software',
        'equipment:edit_user',
        'maintenance:create',
        'history:comment',
        'attachments:upload',
        'history:view', 'attachments:view_all', 'attachments:download' # Necesarios para ver la ficha
    ],
    
    'ADMINISTRADOR CLIENTE': [
        'auth:login',
        # Menú
        'menu:view_client_config',
        # Config Cliente (Tenant)
        'clients:view_self',
        'clients:edit_self_sedes',
        'clients:manage_self_contacts',
        'clients:view_contacts', # Para ver los que crea
        # Dashboard
        'dashboard:view_self',
        # Inventario
        'inventory:view_self', 'inventory:create',
        # Catálogos
        'catalogs:view',
        # Equipo
        'equipment:edit_all', # Gestiona su propio inventario
        'history:view', 'attachments:view_all', 'attachments:download'
    ],

    'SOPORTE CLIENTE': [
        'auth:login',
        # Dashboard
        'dashboard:view_self',
        # Inventario
        'inventory:view_self',
        # Catálogos
        'catalogs:view',
        # Equipo (Solo Lectura)
        'history:view',
        'attachments:view_all', 'attachments:download'
    ],

    'AUDITOR INTERNO': [
        'auth:login', 'auth:2fa_required',
        # Menú
        'menu:view_sys_config', 'menu:view_client_config',
        # Config Sistema
        'sys_company:view', 'sys_users:view_all',
        'catalogs:view', 'catalogs:view_hidden',
        'audit:view_full', 'audit:export',
        # Config Cliente
        'clients:view_list', 'clients:view_details',
        # Dashboard
        'dashboard:view_all', 'dashboard:view_stats',
        # Inventario
        'inventory:view_global', 'inventory:export', 'inventory:export_bulk',
        # Equipo
        'equipment:view_sensitive',
        'history:view', 'history:view_full',
        'attachments:view', 'attachments:view_all', 'attachments:download'
    ],

    'AUDITOR EXTERNO': [
        'auth:login',
        # Menú
        'menu:view_client_config',
        # Config Cliente (Tenant)
        'clients:view_self', 'clients:view_contacts',
        # Dashboard
        'dashboard:view_self',
        # Inventario
        'inventory:view_self', 'inventory:export',
        # Equipo
        'history:view_tenant', # Solo ve cambios de su tenant
        'attachments:view' # Ve adjuntos pero no descarga masiva ni sube
    ]
}

with app.app_context():
    print("Iniciando Seed RBAC...")
    
    # 1. Crear Permisos
    permisos_map = {}
    for code, desc, mod, submod in PERMISOS_DEF:
        p = Permiso.query.filter_by(Codigo=code).first()
        if not p:
            p = Permiso(Codigo=code, Descripcion=desc, Modulo=mod, SubModulo=submod)
            db.session.add(p)
            print(f"Permiso creado: {code}")
        else:
            # Actualizar si ya existe
            p.Descripcion = desc
            p.Modulo = mod
            p.SubModulo = submod
            # print(f"Permiso actualizado: {code}")
            
        permisos_map[code] = p
    db.session.commit()
    
    # 2. Crear Roles y Asignar Permisos
    roles_map = {}
    for r_def in ROLES_DEF:
        r = Rol.query.filter_by(Nombre=r_def['Nombre']).first()
        if not r:
            r = Rol(Nombre=r_def['Nombre'], Scope=r_def['Scope'], Descripcion=r_def['Descripcion'])
            db.session.add(r)
            print(f"Rol creado: {r_def['Nombre']}")
        else:
            # Actualizar scope si cambió
            r.Scope = r_def['Scope']
            
        # Asignar permisos
        if r.Nombre in ROLE_PERMISSIONS:
            codes = ROLE_PERMISSIONS[r.Nombre]
            current_perms = set(p.Codigo for p in r.Permisos)
            for code in codes:
                if code not in current_perms and code in permisos_map:
                    r.Permisos.append(permisos_map[code])
                    
        roles_map[r.Nombre] = r
    db.session.commit()
    
    # 3. Asignar Rol a Usuario Admin
    admin = Persona.query.filter_by(Correo='admin@siicsa.com').first()
    if admin:
        super_admin_rol = roles_map.get('SUPER ADMINISTRADOR')
        if super_admin_rol:
            admin.Rol = super_admin_rol
            db.session.commit()
            print(f"Rol SUPER ADMINISTRADOR asignado a {admin.Correo}")

    print("Seed RBAC finalizado.")
