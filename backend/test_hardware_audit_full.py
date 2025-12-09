import requests
import json
import time

BASE_URL = 'http://127.0.0.1:5000/api'
ADMIN_EMAIL = 'admin@siicsa.com'
ADMIN_PASSWORD = 'AdminPassword123!'

def login():
    try:
        print("Attempting login...")
        # Use 'identifier' instead of 'Correo' based on working script
        res = requests.post(f'{BASE_URL}/auth/login', json={'identifier': ADMIN_EMAIL, 'password': ADMIN_PASSWORD})
        if res.status_code == 200:
            print("Login successful.")
            return res.json().get('token')
        else:
            print(f"Login failed: {res.status_code} {res.text}")
            return None
    except Exception as e:
        print(f"Login error: {e}")
        return None

def run_test():
    token = login()
    if not token:
        return

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    
    # 1. Add RAM
    print("\n--- 1. Adding RAM ---")
    ram_data = {
        'EquipoId': 2,
        'Tipo': 'DDR4',
        'Capacidad': 8,
        'Velocidad': 3200,
        'Marca': 'Kingston',
        'Serial': 'RAM-TEST-001'
    }
    
    # Fetch current
    res_get = requests.get(f'{BASE_URL}/inventory/equipos/2', headers=headers)
    if res_get.status_code != 200:
        print(f"Failed to get equipment: {res_get.status_code}")
        return
        
    equipo = res_get.json()
    if 'Hardware' not in equipo:
        equipo['Hardware'] = {}
        
    current_ram = equipo['Hardware'].get('RAM', [])
    current_ram.append(ram_data)
    
    equipo['Hardware']['RAM'] = current_ram
    
    # Update
    res_put = requests.put(f'{BASE_URL}/inventory/equipos/2', json=equipo, headers=headers)
    print(f"Add RAM Status: {res_put.status_code}")
    if res_put.status_code != 200:
        print(res_put.text)
    
    time.sleep(1)

    # 2. Edit RAM
    print("\n--- 2. Editing RAM ---")
    res_get = requests.get(f'{BASE_URL}/inventory/equipos/2', headers=headers)
    equipo = res_get.json()
    current_ram = equipo.get('Hardware', {}).get('RAM', [])
    target_ram = next((r for r in current_ram if r.get('Serial') == 'RAM-TEST-001'), None)
    
    if target_ram:
        target_ram['Capacidad'] = 16 # Upgrade
        target_ram['Marca'] = 'Kingston Fury'
        
        # PUT
        res_put = requests.put(f'{BASE_URL}/inventory/equipos/2', json=equipo, headers=headers)
        print(f"Edit RAM Status: {res_put.status_code}")
        if res_put.status_code != 200:
            print(res_put.text)
    else:
        print("RAM not found for editing.")

    time.sleep(1)

    # 3. Fetch Logs
    print("\n--- 3. Fetching Logs ---")
    
    # DEBUG: Fetch all logs to see what's happening
    debug_logs = requests.get(f'{BASE_URL}/audit/logs?per_page=10', headers=headers).json().get('data', [])
    print("DEBUG: Latest 5 logs globally:")
    for l in debug_logs[:5]:
        print(f"  [{l.get('Tabla')}] {l.get('Accion')} - Detalle: {l.get('Detalle')}")

    res_logs = requests.get(f'{BASE_URL}/audit/logs?table=Equipos&recordId=2', headers=headers)
    logs_data = res_logs.json()
    logs = logs_data.get('data', [])
    
    print(f"Total Logs Found: {len(logs)}")

    found_create = False
    found_edit = False
    
    for log in logs:
        detalle = log.get('Detalle')
        tabla = log.get('Tabla')
        accion = log.get('Accion')
        
        # We look specifically for changes related to our RAM actions
        # Detailed check
        
    found_create_ram = 0
    found_delete_ram = 0
    
    for log in logs:
        detalle = log.get('Detalle')
        tabla = log.get('Tabla')
        accion = log.get('Accion')
        
        if 'RAM' in str(tabla) or 'EquipoRAM' in str(tabla):
            print(f"RAM Log Found: {accion} - {detalle}")
            
            if accion == 'CREAR':
                found_create_ram += 1
                if '"EquipoId": 2' in detalle or '"EquipoId":2' in detalle:
                     print("  -> CONFIRMED: EquipoId present in CREAR log.")

            if accion == 'ELIMINAR':
                found_delete_ram += 1
                if '"EquipoId": 2' in detalle or '"EquipoId":2' in detalle:
                     print("  -> CONFIRMED: EquipoId present in ELIMINAR log.")

    # We expect at least 1 Create (Step 1) and then 1 Delete + 1 Create (Step 2 update)
    # Total Creates >= 2, Total Deletes >= 1
    
    if found_create_ram >= 2 and found_delete_ram >= 1:
        print("PASS: RAM Create/Delete logs found correctly.")
    else:
        print(f"FAIL: Expected/Found Creates: {found_create_ram}, Deletes: {found_delete_ram}")

if __name__ == '__main__':
    run_test()
