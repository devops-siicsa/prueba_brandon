from app import create_app, db
from app.models.inventory_models import (
    TipoAlmacenamiento, CapacidadAlmacenamiento, 
    ProtocoloAlmacenamiento, FactorFormaAlmacenamiento,
    EquipoAlmacenamiento
)
from sqlalchemy import text

app = create_app()

def run_fix():
    with app.app_context():
        print("Iniciando reparación forzada de tablas de almacenamiento...")
        try:
            # Forzar eliminación de tablas en orden correcto (por dependencias)
            print("Eliminando tablas existentes...")
            
            # Usamos SQL directo para asegurar compatibilidad con SQL Server
            drops = [
                "IF OBJECT_ID(N'[dbo].[EquipoAlmacenamiento]', N'U') IS NOT NULL DROP TABLE [dbo].[EquipoAlmacenamiento]",
                "IF OBJECT_ID(N'[dbo].[ProtocoloAlmacenamiento]', N'U') IS NOT NULL DROP TABLE [dbo].[ProtocoloAlmacenamiento]",
                "IF OBJECT_ID(N'[dbo].[FactorFormaAlmacenamiento]', N'U') IS NOT NULL DROP TABLE [dbo].[FactorFormaAlmacenamiento]",
                "IF OBJECT_ID(N'[dbo].[CapacidadAlmacenamiento]', N'U') IS NOT NULL DROP TABLE [dbo].[CapacidadAlmacenamiento]",
                "IF OBJECT_ID(N'[dbo].[TipoAlmacenamiento]', N'U') IS NOT NULL DROP TABLE [dbo].[TipoAlmacenamiento]"
            ]
            
            with db.engine.connect() as conn:
                for stmt in drops:
                    conn.execute(text(stmt))
                conn.commit()
            
            print("Tablas eliminadas. Recreando esquema...")
            db.create_all()
            print("Esquema creado.")
            
            populate_catalogs()
            
        except Exception as e:
            print(f"ERROR CRÍTICO: {e}")
            import traceback
            traceback.print_exc()

def populate_catalogs():
    print("Poblando catálogos...")
    
    # 1. Tipos
    tipos = ['MECANICO', 'SSD', 'M.2']
    for nombre in tipos:
        db.session.add(TipoAlmacenamiento(Nombre=nombre))
    db.session.commit()
    
    # 2. Capacidades
    capacidades = ['128GB', '240GB', '256GB', '480GB', '500GB', '512GB', '1TB', '2TB', '4TB']
    for cap in capacidades:
        db.session.add(CapacidadAlmacenamiento(Capacidad=cap))
    db.session.commit()
    
    # Helper
    def get_tipo_id(nombre):
        return TipoAlmacenamiento.query.filter_by(Nombre=nombre).first().Id

    id_mecanico = get_tipo_id('MECANICO')
    id_ssd = get_tipo_id('SSD')
    id_m2 = get_tipo_id('M.2')

    # 3. Protocolos
    protocolos = [
        ('SATA', id_mecanico),
        ('SATA', id_ssd),
        ('SATA', id_m2),
        ('PCIe', id_m2),
        ('NVMe', id_m2)
    ]
    for nombre, tipo_id in protocolos:
        db.session.add(ProtocoloAlmacenamiento(Nombre=nombre, TipoId=tipo_id))
    db.session.commit()

    # 4. Factores de Forma
    factores = [
        ('3.5', id_mecanico),
        ('2.5', id_mecanico),
        ('2.5', id_ssd),
        ('2280', id_m2),
        ('2242', id_m2),
        ('2230', id_m2),
        ('22110', id_m2)
    ]
    for nombre, tipo_id in factores:
        db.session.add(FactorFormaAlmacenamiento(Nombre=nombre, TipoId=tipo_id))
    db.session.commit()
    print("Catálogos poblados exitosamente.")

if __name__ == '__main__':
    run_fix()
