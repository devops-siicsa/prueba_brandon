import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import create_app
from app.extensions import db
from app.models.inventory_models import EquipoAplicacion
from app.models.core_models import Aplicacion

app = create_app()
with app.app_context():
    try:
        print("Testing JOIN query...")
        
        # Test the exact query from the route
        equipo_id = 2
        apps_query = db.session.query(EquipoAplicacion, Aplicacion).outerjoin(Aplicacion, EquipoAplicacion.AplicacionId == Aplicacion.Id).filter(EquipoAplicacion.EquipoId == equipo_id).all()
        
        print(f"✓ Query successful! Found {len(apps_query)} applications")
        
        for ea, app in apps_query:
            print(f"  - EquipoAplicacion ID: {ea.Id}, AplicacionId: {ea.AplicacionId}")
            if app:
                print(f"    Aplicacion: {app.Nombre} (v{app.Version})")
            else:
                print(f"    Aplicacion: NULL (orphan record)")
                
    except Exception as e:
        print(f"✗ Error: {type(e).__name__}")
        print(f"  Message: {str(e)}")
        import traceback
        traceback.print_exc()
