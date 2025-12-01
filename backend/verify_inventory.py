import requests
import json

BASE_URL = 'http://localhost:5000/api'

def login():
    # Assuming a default admin user exists or was created in previous steps
    # If not, we might need to create one or use existing credentials
    # Using a placeholder credential based on common defaults or previous context
    # If this fails, I'll need to know valid credentials
    payload = {
        'username': 'admin', 
        'password': 'password123' # Replace with actual if known, or I'll need to check how to get a token
    }
    # Actually, I don't have the credentials handy. 
    # Let's try to register a new user or use a known one if possible.
    # Alternatively, I can bypass auth for testing if I disable the decorator temporarily, but that's risky.
    # Let's try to login with 'admin' / 'admin' or similar.
    
    # Better approach: Check if I can create a user first or if I can inspect the DB.
    # For now, let's assume I can't easily login without knowing the seed data.
    # But wait, I can check `backend/app/commands.py` or similar to see seed data.
    pass

# Since I don't have the credentials, I will create a script that interacts with the app context directly
# to bypass the HTTP auth layer for unit testing purposes, OR I will try to find the credentials.
# Let's look at `backend/app/routes/auth_routes.py` or `seed.py` if it exists.

# Actually, I will write a script that imports the app and creates a test context.
# This is more reliable than HTTP requests without known credentials.

from app import create_app
from app.extensions import db
from app.models.inventory_models import Equipo, EquipoProcesador
from app.models.auth_models import Persona # Assuming this exists
from flask import json

app = create_app()

def verify_inventory_logic():
    with app.app_context():
        print("Verifying Inventory Logic...")
        
        # 1. Create a dummy equipment
        # We need a user ID for 'CreadoPorId'
        # Let's just use 1
        
        # Cleanup first
        Equipo.query.filter_by(CodigoEquipo='TEST-001').delete()
        db.session.commit()
        
        print("Creating Equipment...")
        new_equipo = Equipo(
            CodigoEquipo='TEST-001',
            Modelo='Test Model',
            Serial='SN-12345',
            CreadoPorId=1
        )
        db.session.add(new_equipo)
        db.session.commit()
        
        equipo_id = new_equipo.Id
        print(f"Equipment Created with ID: {equipo_id}")
        
        # 2. Add Related Data (Processor)
        print("Adding Processor...")
        # We need a GeneracionId. Let's assume one exists or create a dummy one.
        # For this test, we might fail if catalogs are empty.
        # Let's check catalogs.
        from app.models.inventory_models import GeneracionProcesador
        gen = GeneracionProcesador.query.first()
        if not gen:
            print("No GeneracionProcesador found. Skipping processor test.")
        else:
            proc = EquipoProcesador(EquipoId=equipo_id, GeneracionId=gen.Id)
            db.session.add(proc)
            db.session.commit()
            print("Processor Added.")
            
        # 3. Verify Data Retrieval
        print("Verifying Retrieval...")
        equipo = Equipo.query.get(equipo_id)
        if equipo and equipo.CodigoEquipo == 'TEST-001':
            print("SUCCESS: Equipment retrieved correctly.")
        else:
            print("FAILURE: Equipment not found or incorrect.")
            
        # 4. Verify Related Data
        procs = EquipoProcesador.query.filter_by(EquipoId=equipo_id).all()
        if gen and len(procs) > 0:
             print("SUCCESS: Processor retrieved correctly.")
        elif gen:
             print("FAILURE: Processor not found.")
             
        # Cleanup
        print("Cleaning up...")
        EquipoProcesador.query.filter_by(EquipoId=equipo_id).delete()
        Equipo.query.filter_by(Id=equipo_id).delete()
        db.session.commit()
        print("Done.")

if __name__ == '__main__':
    verify_inventory_logic()
