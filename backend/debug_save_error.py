import requests
import json

BASE_URL = "http://127.0.0.1:5000/api"

def login():
    resp = requests.post(f"{BASE_URL}/auth/login", json={
        "identifier": "admin@siicsa.com",
        "password": "AdminPassword123!"
    })
    if resp.status_code != 200:
        print(f"Login failed: {resp.status_code} - {resp.text}")
        return None
    return resp.json()['token']

def test_update_processor():
    token = login()
    headers = {"Authorization": f"Bearer {token}"}
    
    # Fetch random equipment or create one?
    # Let's try ID 2 as seen in screenshot "TEST_APPS"
    equipo_id = 2
    
    # URL
    url = f"{BASE_URL}/inventory/equipos/{equipo_id}"
    
    # Payload similar to what frontend sends
    # Based on screenshot: Hardware -> Procesador
    payload = {
        "Procesadores": [
            {"GeneracionId": 1, "MarcaId": 1, "TipoId": 1} # Guessing structure
        ],
        # Include minimal other fields to avoid validation errors if any
        "MemoriasRAM": [],
        "Almacenamiento": [], 
        "Aplicativos": []
    }
    
    print(f"Sending PUT to {url} with payload: {json.dumps(payload, indent=2)}")
    
    resp = requests.put(url, json=payload, headers=headers)
    print(f"Status Code: {resp.status_code}")
    print(f"Response Body: {resp.text}")

if __name__ == "__main__":
    try:
        test_update_processor()
    except Exception as e:
        print(e)
