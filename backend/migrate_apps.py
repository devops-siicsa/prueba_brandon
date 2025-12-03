from app import create_app, db
from sqlalchemy import text

app = create_app()

with app.app_context():
    try:
        # Check if column exists
        check_sql = text("SELECT COL_LENGTH('Aplicaciones', 'Version')")
        result = db.session.execute(check_sql).scalar()
        
        if result is None:
            print("Adding Version column to Aplicaciones table...")
            alter_sql = text("ALTER TABLE Aplicaciones ADD Version NVARCHAR(50)")
            db.session.execute(alter_sql)
            db.session.commit()
            print("Column added successfully.")
        else:
            print("Column Version already exists.")
            
    except Exception as e:
        print(f"Error: {e}")
