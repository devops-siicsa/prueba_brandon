from app import create_app, db
from sqlalchemy import text

app = create_app()

with app.app_context():
    try:
        # Check if column exists first to avoid error
        check_query = text("SELECT COL_LENGTH('Equipos', 'SedeId')")
        result = db.session.execute(check_query).scalar()
        
        if result is None:
            print("Adding SedeId column to Equipos table...")
            alter_query = text("ALTER TABLE Equipos ADD SedeId INT FOREIGN KEY REFERENCES Sedes(Id)")
            db.session.execute(alter_query)
            db.session.commit()
            print("Migration successful: SedeId column added.")
        else:
            print("SedeId column already exists.")
            
    except Exception as e:
        print(f"Error executing migration: {e}")
