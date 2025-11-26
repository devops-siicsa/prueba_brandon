import requests
import json

BASE_URL = 'http://127.0.0.1:5000/api'
ADMIN_EMAIL = 'admin@siicsa.com'
ADMIN_PASSWORD = 'AdminPassword123!'

def test_granular_permissions():
    session = requests.Session()
    
    # 1. Login Admin
    print("1. Login Admin...")
    resp = session.post(f'{BASE_URL}/auth/login', json={
        'identifier': ADMIN_EMAIL,
        'password': ADMIN_PASSWORD
    })
    if resp.status_code != 200:
        print("Error login admin:", resp.text)
        return
    print("Login Admin OK")

    # 2. Obtener Permisos
    print("\n2. Obteniendo lista de permisos...")
    resp = session.get(f'{BASE_URL}/config/permissions')
    if resp.status_code != 200:
        print("Error obteniendo permisos:", resp.text)
        return
    permissions = resp.json()
    print(f"Permisos encontrados: {len(permissions)}")
    if not permissions:
        print("No hay permisos para probar.")
        return
        
    # Seleccionar un permiso para asignar (ej: el primero)
    permiso_prueba = permissions[0]
    print(f"Permiso seleccionado para prueba: {permiso_prueba['Codigo']} (ID: {permiso_prueba['Id']})")

    # 3. Crear Usuario con Permiso Específico
    print("\n3. Creando usuario con permiso específico...")
    new_user_data = {
        'Nombre': 'Usuario',
        'Apellido': 'Granular',
        'Correo': 'granular@test.com',
        'Password': 'User123!',
        'EsUsuarioSistema': True,
        'RolId': None, # Sin Rol para probar solo permiso específico (o con rol básico)
        # Asumimos que existe un rol básico o lo dejamos null si el modelo lo permite (RolId es FK, nullable?)
        # Revisando modelo: RolId es FK, pero en create_user es opcional.
        # Vamos a asignarle un rol si es obligatorio, o null.
        # Probemos null primero.
        'PermisosEspecificos': [permiso_prueba['Id']]
    }
    
    # Necesitamos un RolId válido si es obligatorio.
    # Obtener roles
    roles_resp = session.get(f'{BASE_URL}/config/roles')
    roles = roles_resp.json()
    if roles:
        new_user_data['RolId'] = roles[0]['Id'] # Asignar primer rol disponible
        print(f"Asignando Rol: {roles[0]['Nombre']}")
        
    resp = session.post(f'{BASE_URL}/config/users', json=new_user_data)
    if resp.status_code == 201:
        user_id = resp.json()['Id']
        print(f"Usuario creado ID: {user_id}")
    else:
        # Si falla por correo duplicado, intentar actualizar o ignorar
        print("Error creando usuario (puede que ya exista):", resp.text)
        # Intentar obtener el usuario para actualizarlo
        # (Omitido por simplicidad, asumimos base limpia o correo único)
        return

    # 4. Login con Nuevo Usuario
    print("\n4. Login con Usuario Granular...")
    user_session = requests.Session()
    resp = user_session.post(f'{BASE_URL}/auth/login', json={
        'identifier': 'granular@test.com',
        'password': 'User123!'
    })
    
    if resp.status_code == 200:
        data = resp.json()
        user_perms = data['user']['Permisos']
        print(f"Login OK. Permisos del usuario: {user_perms}")
        
        if permiso_prueba['Codigo'] in user_perms:
            print("✅ ÉXITO: El permiso específico está presente.")
        else:
            print("❌ FALLO: El permiso específico NO está presente.")
    else:
        print("Error login usuario granular:", resp.text)

if __name__ == '__main__':
    test_granular_permissions()
