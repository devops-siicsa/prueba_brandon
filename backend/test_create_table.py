from app import create_app, db
from sqlalchemy import text

app = create_app()

def run_test():
    with app.app_context():
        print("Probando creación de tabla dummy...")
        try:
            with db.engine.connect() as conn:
                conn.execute(text("CREATE TABLE TestTable (Id INT PRIMARY KEY, Nombre NVARCHAR(50))"))
                conn.commit()
            print("Tabla TestTable creada exitosamente.")
            
            with db.engine.connect() as conn:
                conn.execute(text("DROP TABLE TestTable"))
                conn.commit()
            print("Tabla TestTable eliminada exitosamente.")
            
        except Exception as e:
            print(f"ERROR DE PERMISOS O CONEXIÓN: {e}")

if __name__ == '__main__':
    run_test()
