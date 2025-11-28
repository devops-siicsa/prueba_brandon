from app import create_app, db
from app.models.inventory_models import TipoAlmacenamiento

app = create_app()

def debug():
    with app.app_context():
        print("Probando consulta a TipoAlmacenamiento...")
        try:
            items = TipoAlmacenamiento.query.all()
            print(f"Éxito. Encontrados {len(items)} items.")
            for i in items:
                print(f"- {i.Nombre} (Activo: {i.Activo})")
        except Exception as e:
            print(f"ERROR: {e}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    debug()
