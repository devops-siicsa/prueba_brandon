import requests
try:
    print("Enviando petición de login CORRECTO...")
    res = requests.post('http://127.0.0.1:5000/api/auth/login', json={"identifier": "admin@siicsa.com", "password": "AdminPassword123!"})
    print(f"Status: {res.status_code}")
    print(f"Body: {res.text}")
    print(f"Cookies: {res.cookies.get_dict()}")
except Exception as e:
    print(f"Error: {e}")
