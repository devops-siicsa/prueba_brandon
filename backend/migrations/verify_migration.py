"""
Script de verificación post-migración para el sistema de aplicativos
Verifica que la migración se completó correctamente y que la funcionalidad está operativa
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import create_app
from app.extensions import db
from app.models.inventory_models import EquipoAplicacion
from app.models.core_models import Aplicacion
from sqlalchemy import text

def verify_migration():
    app = create_app()
    
    with app.app_context():
        print("="*70)
        print("VERIFICACIÓN POST-MIGRACIÓN: Sistema de Aplicativos")
        print("="*70)
        
        # 1. Verificar estructura de tabla
        print("\n[1/5] Verificando estructura de la tabla EquipoAplicaciones...")
        try:
            columns = db.session.execute(text("DESCRIBE EquipoAplicaciones")).fetchall()
            column_names = [col[0] for col in columns]
            
            if 'AplicacionId' in column_names:
                print("  ✓ Columna 'AplicacionId' existe")
            else:
                print("  ✗ ERROR: Columna 'AplicacionId' NO existe")
                return False
            
            if 'NombreAplicacion' not in column_names:
                print("  ✓ Columna 'NombreAplicacion' fue eliminada correctamente")
            else:
                print("  ✗ ERROR: Columna 'NombreAplicacion' aún existe (basura no eliminada)")
                return False
                
        except Exception as e:
            print(f"  ✗ Error verificando estructura: {e}")
            return False
        
        # 2. Verificar foreign key constraint
        print("\n[2/5] Verificando foreign key constraint...")
        try:
            fk_query = text("""
                SELECT CONSTRAINT_NAME 
                FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
                WHERE TABLE_SCHEMA = 'sistema_inventario' 
                  AND TABLE_NAME = 'EquipoAplicaciones'
                  AND REFERENCED_TABLE_NAME = 'Aplicaciones'
            """)
            fks = db.session.execute(fk_query).fetchall()
            
            if fks and len(fks) > 0:
                print(f"  ✓ Foreign key constraint existe: {fks[0][0]}")
            else:
                print("  ✗ ERROR: Foreign key constraint NO existe")
                return False
                
        except Exception as e:
            print(f"  ✗ Error verificando foreign key: {e}")
            return False
        
        # 3. Verificar modelo de SQLAlchemy
        print("\n[3/5] Verificando modelo de SQLAlchemy...")
        try:
            # Verificar que el modelo tenga AplicacionId
            if hasattr(EquipoAplicacion, 'AplicacionId'):
                print("  ✓ Modelo tiene atributo 'AplicacionId'")
            else:
                print("  ✗ ERROR: Modelo NO tiene atributo 'AplicacionId'")
                return False
            
            # Verificar que el modelo NO tenga NombreAplicacion
            if not hasattr(EquipoAplicacion, 'NombreAplicacion'):
                print("  ✓ Modelo NO tiene atributo 'NombreAplicacion' (limpio)")
            else:
                print("  ✗ ERROR: Modelo aún tiene atributo 'NombreAplicacion' (basura)")
                return False
            
            # Verificar relationship
            if hasattr(EquipoAplicacion, 'Aplicacion'):
                print("  ✓ Modelo tiene relationship 'Aplicacion'")
            else:
                print("  ⚠ ADVERTENCIA: Modelo NO tiene relationship 'Aplicacion'")
                
        except Exception as e:
            print(f"  ✗ Error verificando modelo: {e}")
            return False
        
        # 4. Verificar integridad de datos
        print("\n[4/5] Verificando integridad de datos...")
        try:
            total_equipo_apps = EquipoAplicacion.query.count()
            print(f"  • Total de asignaciones de aplicaciones: {total_equipo_apps}")
            
            # Verificar que todas las asignaciones tienen AplicacionId válido
            invalid = db.session.execute(text("""
                SELECT COUNT(*) 
                FROM EquipoAplicaciones ea
                LEFT JOIN Aplicaciones a ON ea.AplicacionId = a.Id
                WHERE a.Id IS NULL
            """)).fetchone()[0]
            
            if invalid == 0:
                print("  ✓ Todas las asignaciones tienen AplicacionId válido")
            else:
                print(f"  ✗ ERROR: {invalid} asignaciones con AplicacionId inválido")
                return False
                
        except Exception as e:
            print(f"  ✗ Error verificando integridad: {e}")
            return False
        
        # 5. Test de funcionalidad básica
        print("\n[5/5] Probando funcionalidad básica...")
        try:
            # Intentar leer aplicaciones con su catálogo
            sample = EquipoAplicacion.query.first()
            if sample:
                print(f"  • Asignación de ejemplo (ID {sample.Id}):")
                print(f"    - EquipoId: {sample.EquipoId}")
                print(f"    - AplicacionId: {sample.AplicacionId}")
                if sample.Aplicacion:
                    print(f"    - Aplicación (via relationship): {sample.Aplicacion.Nombre}")
                    print("  ✓ Relationship funciona correctamente")
                else:
                    print("  ⚠ ADVERTENCIA: Relationship no retorna datos")
            else:
                print("  • No hay datos de prueba disponibles")
                
        except Exception as e:
            print(f"  ✗ Error probando funcionalidad: {e}")
            return False
        
        print("\n" + "="*70)
        print("✓ VERIFICACIÓN COMPLETADA EXITOSAMENTE")
        print("="*70)
        print("\nResumen:")
        print("  • Estructura de BD correcta")
        print("  • Foreign key establecido")
        print("  • Modelo actualizado (sin basura)")
        print("  • Datos con integridad referencial")
        print("  • Funcionalidad operativa")
        print("\nEl sistema de aplicativos está listo para usar.")
        print("="*70)
        
        return True

if __name__ == '__main__':
    success = verify_migration()
    sys.exit(0 if success else 1)
