import requests
import json

BASE_URL = "http://127.0.0.1:5000/api"

def test_chain():
    print("--- TESTING FULL API CHAIN ---")
    
    # 1. Login
    print(f"1. Attempting Login to {BASE_URL}/auth/login...")
    try:
        resp = requests.post(f"{BASE_URL}/auth/login", json={
            "identifier": "admin@siicsa.com",
            "password": "AdminPassword123!"
        })
        print(f"   Status: {resp.status_code}")
        if resp.status_code != 200:
            print(f"   Error: {resp.text}")
            return
            
        data = resp.json()
        token = data.get('token')
        if not token:
            print("   ERROR: Token is None or empty!")
            return
        print(f"   Login Successful. Token received: {token[:10]}...")
    except Exception as e:
        print(f"   Login Failed: {e}")
        return

    # 2. Fetch Audit Logs
    print(f"\n2. Attempting to Fetch Logs from {BASE_URL}/audit/logs...")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        resp = requests.get(f"{BASE_URL}/audit/logs", headers=headers, params={"page": 1, "per_page": 10})
        
        print(f"   Status: {resp.status_code}")
        if resp.status_code == 200:
            logs = resp.json().get('logs', [])
            total = resp.json().get('total', 0)
            print(f"   Success! Found {len(logs)} logs (Total: {total}).")
            if len(logs) > 0:
                print(f"   Sample Log: {logs[0]['Accion']} on {logs[0]['Tabla']}")
        else:
            print(f"   Failed. Response: {resp.text}")
            
    except Exception as e:
        print(f"   Fetch Failed: {e}")

if __name__ == "__main__":
    test_chain()
