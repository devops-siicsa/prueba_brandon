import requests
import json
import time

BASE_URL = 'http://127.0.0.1:5000/api'

def login():
    try:
        print("Attempting login...")
        payload = {"identifier": "admin@siicsa.com", "password": "AdminPassword123!"} 
        res = requests.post(f'{BASE_URL}/auth/login', json=payload)
        if res.status_code == 200:
            print("Login successful.")
            return res.json()['token']
        print(f"Login failed: {res.status_code} {res.text}")
        return None
    except Exception as e:
        print(f"Login exception: {e}")
        return None

def test_equipment_update(token):
    headers = {'Authorization': f'Bearer {token}'}
    print(f"\n--- Testing: Update Equipment Fields ---")
    
    # 1. Get current
    res = requests.get(f'{BASE_URL}/inventory/equipos/2', headers=headers)
    if res.status_code != 200:
        print(f"Failed to get equipment: {res.status_code}")
        return

    current = res.json()
    print(f"Current Serial: {current.get('Serial')}")
    
    # 2. Update Serial
    current_serial = str(current.get('Serial', 'SER-100'))
    new_serial_num = 100
    if '-' in current_serial:
        try:
            new_serial_num = int(current_serial.split('-')[-1]) + 1
        except:
            pass
    new_serial = f"SER-{new_serial_num}"
            
    payload = {
        "Serial": new_serial,
        "Modelo": f"Dell Optiplex Mod {new_serial_num}"
    }
    
    print(f"Updating to Serial: {new_serial}")
    res = requests.put(f'{BASE_URL}/inventory/equipos/2', json=payload, headers=headers)
    print(f"Update Status: {res.status_code}")
    
    time.sleep(1) # Wait for async logs if any (unlikely inside transaction but good practice)

    # 3. Check Audit Logs
    res_logs = requests.get(f'{BASE_URL}/audit/logs?table=Equipos&record_id=2', headers=headers)
    logs = res_logs.json()
    
    print(f"Logs keys: {logs.keys()}")
    print(f"Logs['data'] len: {len(logs.get('data', []))}")
    print(f"Logs['logs'] len: {len(logs.get('logs', []))}")
    
    log_list = logs.get('logs', []) or logs.get('data', [])
    
    # Find the latest log
    if log_list and len(log_list) > 0:
        latest = log_list[0]
        print(f"Latest Log Action: {latest.get('Accion')}")
        print(f"Latest Log Detail (RAW): {latest.get('Detalle')}")
    else:
        print("No logs found.")

if __name__ == '__main__':
    token = login()
    if token:
        test_equipment_update(token)
