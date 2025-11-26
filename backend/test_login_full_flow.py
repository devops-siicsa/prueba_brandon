import requests
import json

BASE_URL = 'http://127.0.0.1:5000/api'
LOGIN_URL = f'{BASE_URL}/auth/login'
CONFIG_URL = f'{BASE_URL}/config/companies'

session = requests.Session()

print(f"Intentando login en {LOGIN_URL}...")
try:
    response = session.post(LOGIN_URL, json={
        'identifier': 'admin@siicsa.com',
        'password': 'AdminPassword123!'
    })
    
    print(f"Status Code Login: {response.status_code}")
    print(f"Response Login: {response.text}")
    print(f"Cookies: {session.cookies.get_dict()}")
    
    if response.status_code == 200:
        print("\nLogin exitoso. Intentando acceder a Configuración...")
        config_response = session.get(CONFIG_URL)
        print(f"Status Code Config: {config_response.status_code}")
        print(f"Response Config: {config_response.text}")
    else:
        print("Login fallido.")

except Exception as e:
    print(f"Error de conexión: {e}")
