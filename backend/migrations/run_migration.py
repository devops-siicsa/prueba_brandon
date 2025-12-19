"""
Script para ejecutar la migración de la tabla EquipoAplicaciones
Este script ejecuta el archivo SQL de migración de manera segura
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import create_app
from app.extensions import db
from sqlalchemy import text

def run_migration():
    app = create_app()
    
    with app.app_context():
        print("="*70)
        print("INICIANDO MIGRACIÓN: EquipoAplicaciones")
        print("="*70)
        
        # Leer el archivo SQL
        migration_file = os.path.join(os.path.dirname(__file__), 'migration_aplicaciones.sql')
        
        with open(migration_file, 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        # Dividir en statements individuales y ejecutar
        statements = [s.strip() for s in sql_content.split(';') if s.strip() and not s.strip().startswith('--')]
        
        try:
            for i, statement in enumerate(statements, 1):
                if statement:
                    print(f"\n[{i}/{len(statements)}] Ejecutando statement...")
                    result = db.session.execute(text(statement))
                    
                    # Si es un SELECT, mostrar resultados
                    if statement.strip().upper().startswith('SELECT'):
                        rows = result.fetchall()
                        if rows:
                            for row in rows:
                                print(f"  → {dict(row._mapping)}")
                    
                    db.session.commit()
            
            print("\n" + "="*70)
            print("✓ MIGRACIÓN COMPLETADA EXITOSAMENTE")
            print("="*70)
            
        except Exception as e:
            db.session.rollback()
            print("\n" + "="*70)
            print("✗ ERROR EN LA MIGRACIÓN")
            print("="*70)
            print(f"Error: {str(e)}")
            return False
        
        return True

if __name__ == '__main__':
    success = run_migration()
    sys.exit(0 if success else 1)
