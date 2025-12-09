import requests
import json

BASE_URL = 'http://127.0.0.1:5000/api'

def login():
    try:
        # Try admin first (from screenshot)
        payload = {"identifier": "admin@siicsa.com", "password": "AdminPassword123!"} 
        res = requests.post(f'{BASE_URL}/auth/login', json=payload)
        if res.status_code == 200:
            return res.json()['token']
        
        # Try test user
        payload = {"identifier": "test", "password": "test"}
        res = requests.post(f'{BASE_URL}/auth/login', json=payload)
        if res.status_code == 200:
            return res.json()['token']
        
        print(f"Login failed: {res.status_code} {res.text}")
        return None
    except Exception as e:
        print(f"Login error: {e}")
        return None

def test_update(token, payload, description):
    headers = {'Authorization': f'Bearer {token}'}
    print(f"\n--- Testing: {description} ---")
    print(f"Payload: {json.dumps(payload, indent=2)}")
    try:
        res = requests.put(f'{BASE_URL}/inventory/equipos/2', json=payload, headers=headers)
        print(f"Status: {res.status_code}")
        print(f"Response: {res.text}")
    except Exception as e:
        print(f"Request Error: {e}")

token = login()
if token:
    # Test 1: Cargo as String (Manual Type)
    test_update(token, {"Cargo": "ManualString", "UsuarioAsignadoId": 1}, "Cargo as String")

    # Test 2: Cargo as Dict (Select existing)
    test_update(token, {"Cargo": {"Id": 1, "Nombre": "Gerencia"}, "UsuarioAsignadoId": 1}, "Cargo as Dict")

    # Test 3: Cargo as Dict with missing name
    test_update(token, {"Cargo": {"Id": 1}, "UsuarioAsignadoId": 1}, "Cargo as Dict (No Name)")
    
    # Test 4: Mixed Area as String
    test_update(token, {"Area": "ManualArea", "UsuarioAsignadoId": 1}, "Area as String")

    # Test 5: Mixed Area as Dict
    test_update(token, {"Area": {"Id": 1, "Nombre": "Admin"}, "UsuarioAsignadoId": 1}, "Area as Dict")

    # Test 6: Apps as Objects (Regression Check)
    test_update(token, {
        "CodigoEquipo": "TEST_APPS", 
        "Aplicativos": [{"Id": 1, "Nombre": "Office", "Version": "365"}]
    }, "Apps as Objects")
