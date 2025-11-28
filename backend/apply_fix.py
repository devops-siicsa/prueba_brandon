from app import create_app, db
from sqlalchemy import text

app = create_app()

def run_fix():
    with app.app_context():
        print("Conectando a la base de datos...")
        try:
            with open('fix_storage_tables.sql', 'r') as f:
                sql_content = f.read()
            
            # Split by commands if necessary, but sqlalchemy execute might handle blocks
            # T-SQL scripts often need splitting by GO, but this file doesn't have GO.
            # However, sqlalchemy might struggle with multiple statements in one go depending on the driver.
            # Let's try executing the whole block first.
            
            print("Ejecutando script SQL...")
            with db.engine.connect() as connection:
                # Use raw connection for DDL script execution if needed, or text()
                # Splitting by semicolon might be safer for simple statements
                statements = sql_content.split(';')
                for statement in statements:
                    if statement.strip():
                        print(f"Ejecutando: {statement[:50]}...")
                        connection.execute(text(statement))
                        connection.commit()
                
            print("Script ejecutado exitosamente.")
        except Exception as e:
            print(f"Error ejecutando script: {e}")

if __name__ == '__main__':
    run_fix()
