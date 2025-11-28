from app import create_app, db
from app.models.inventory_models import (
    TipoAlmacenamiento, CapacidadAlmacenamiento, 
    ProtocoloAlmacenamiento, FactorFormaAlmacenamiento
)

app = create_app()

def run_fix():
    with app.app_context():
        print("Intentando poblar catálogos de almacenamiento...")
        try:
            # 1. Tipos
            tipos = ['MECANICO', 'SSD', 'M.2']
            for nombre in tipos:
                if not TipoAlmacenamiento.query.filter_by(Nombre=nombre).first():
                    print(f"Creando Tipo: {nombre}")
                    db.session.add(TipoAlmacenamiento(Nombre=nombre))
            db.session.commit()
            
            # 2. Capacidades
            capacidades = ['128GB', '240GB', '256GB', '480GB', '500GB', '512GB', '1TB', '2TB', '4TB']
            for cap in capacidades:
                if not CapacidadAlmacenamiento.query.filter_by(Capacidad=cap).first():
                    print(f"Creando Capacidad: {cap}")
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
                if not ProtocoloAlmacenamiento.query.filter_by(Nombre=nombre, TipoId=tipo_id).first():
                    print(f"Creando Protocolo: {nombre}")
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
                if not FactorFormaAlmacenamiento.query.filter_by(Nombre=nombre, TipoId=tipo_id).first():
                    print(f"Creando Factor Forma: {nombre}")
                    db.session.add(FactorFormaAlmacenamiento(Nombre=nombre, TipoId=tipo_id))
            db.session.commit()
            print("Catálogos verificados/poblados exitosamente.")
            
        except Exception as e:
            print(f"ERROR: {e}")

if __name__ == '__main__':
    run_fix()
