import pyodbc
from configuracionbd import get_db_connection

try:
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Primero, obtener las tablas disponibles
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' ORDER BY TABLE_NAME")
    tablas = [row[0] for row in cursor.fetchall()]
    
    print("=" * 80)
    print("TABLAS ENCONTRADAS EN LA BASE DE DATOS:")
    print("=" * 80)
    for tabla in tablas:
        if 'comercial' in tabla.lower() or 'usuario' in tabla.lower() or 'cargo' in tabla.lower():
            print(f"  ✓ {tabla}")
    print()
    
    # Buscar tabla de comerciales/usuarios
    tabla_usuarios = None
    for t in tablas:
        if 'comercial' in t.lower() and 'estado' not in t.lower() and 'producto' not in t.lower():
            tabla_usuarios = t
            break
    
    if not tabla_usuarios:
        print("No se encontró tabla de usuarios/comerciales. Usando stored procedure procLogin...")
        # Intentar obtener estructura del SP
        cursor.execute("EXEC sp_helptext 'procLogin'")
        sp_text = cursor.fetchall()
        print("\nContenido del SP procLogin:")
        print("-" * 80)
        for line in sp_text:
            print(line[0])
        cursor.close()
        conn.close()
        exit()
    
    # Obtener estructura de tablas relevantes
    print("=" * 80)
    cursor.execute("SELECT TOP 1 * FROM usuario")
    columnas_usuario = [column[0] for column in cursor.description]
    print("Columnas de 'usuario':", ", ".join(columnas_usuario))
    
    cursor.execute("SELECT TOP 1 * FROM usuario_x_cargo")
    columnas_uxc = [column[0] for column in cursor.description]
    print("Columnas de 'usuario_x_cargo':", ", ".join(columnas_uxc))
    
    cursor.execute("SELECT TOP 1 * FROM cargo")
    columnas_cargo = [column[0] for column in cursor.description]
    print("Columnas de 'cargo':", ", ".join(columnas_cargo))
    print("=" * 80)
    print()
    
    # Columnas reales según la salida: 'idusu', 'idcarg'
    # Consultar tabla de usuarios con sus cargos
    query = """
    SELECT TOP 100
        u.id,
        u.nombre,
        u.apellido,
        u.correo,
        u.cuenta,
        uxc.idcarg as idCargo,
        c.nombre as nombreCargo
    FROM usuario u
    LEFT JOIN usuario_x_cargo uxc ON u.id = uxc.idusu
    LEFT JOIN cargo c ON uxc.idcarg = c.id
    WHERE u.activo = 1
    ORDER BY uxc.idcarg, u.nombre
    """
    
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    
    print("=" * 80)
    print("ANÁLISIS DE USUARIOS Y ROLES EN LA BASE DE DATOS")
    print("=" * 80)
    print()
    
    usuarios = cursor.fetchall()
    
    print(f"Tabla utilizada: {tabla_usuarios}")
    print()
    
    # Agrupar por idCargo
    roles_dict = {}
    for row in usuarios:
        id_cargo = row.idCargo if row.idCargo else 0
        nombre_cargo = row.nombreCargo if row.nombreCargo else 'Sin Cargo'
        
        if id_cargo not in roles_dict:
            roles_dict[id_cargo] = {'nombreCargo': nombre_cargo, 'usuarios': []}
        
        roles_dict[id_cargo]['usuarios'].append({
            'id': row.id,
            'correo': row.correo,
            'cuenta': row.cuenta,
            'nombre': f"{row.nombre} {row.apellido}".strip()
        })
    
    # Mostrar resultados agrupados
    for id_cargo in sorted(roles_dict.keys()):
        info_cargo = roles_dict[id_cargo]
        nombre_cargo = info_cargo['nombreCargo']
        usuarios_cargo = info_cargo['usuarios']
        
        print(f"idCargo = {id_cargo} → {nombre_cargo}")
        print("-" * 80)
        for u in usuarios_cargo:
            cuenta_str = u['cuenta'] if u['cuenta'] else 'N/A'
            print(f"  • Cuenta: {cuenta_str:20} | Correo: {u['correo']:30} | Nombre: {u['nombre']:35} | ID: {u['id']}")
        print()
    
    cursor.close()
    conn.close()
    
    print("=" * 80)
    print(f"Total de usuarios encontrados: {len(usuarios)}")
    print("=" * 80)
    
except Exception as e:
    print(f"Error al consultar la base de datos: {e}")
    import traceback
    traceback.print_exc()
