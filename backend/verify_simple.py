from app import create_app, db
from app.models.inventory_models import TipoRAM

app = create_app()

with app.app_context():
    print("--- Verificando Simple ---")
    try:
        nuevo = TipoRAM(Nombre="SimpleTestRAM")
        db.session.add(nuevo)
        db.session.commit()
        print("Insert exitoso")
        
        db.session.delete(nuevo)
        db.session.commit()
        print("Delete exitoso")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
