from app import create_app, db
from app.models.inventory_models import EquipoRAM, BusRAM, TipoRAM
from sqlalchemy import text

app = create_app()

with app.app_context():
    print(f"Inspecting RAM for CodigoEquipo: 6841")
    from app.models.inventory_models import Equipo
    
    equipo = Equipo.query.filter_by(CodigoEquipo='6841').first()
    if not equipo:
        print("Equipo not found with code 6841")
    else:
        print(f"Found Equipo ID: {equipo.Id}")
        ram_entries = EquipoRAM.query.filter_by(EquipoId=equipo.Id).all()
    
    if not ram_entries:
        print("No RAM entries found.")
    
    for ram in ram_entries:
        print(f"RAM Entry ID: {ram.Id}")
        print(f"  BusId: {ram.BusId}")
        print(f"  CapacidadId: {ram.CapacidadId}")
        
        if ram.BusId:
            bus = BusRAM.query.get(ram.BusId)
            if bus:
                print(f"    Bus Found: {bus.Velocidad} (ID: {bus.Id})")
                print(f"    Bus.TipoId: {bus.TipoId}")
                
                if bus.TipoId:
                    tipo = TipoRAM.query.get(bus.TipoId)
                    if tipo:
                        print(f"      Tipo Found: {tipo.Nombre} (ID: {tipo.Id})")
                    else:
                        print("      Tipo NOT found via Bus.")
                else:
                    print("    Bus has NO TipoId.")
            else:
                print("    Bus NOT found in BusRAM table.")
        else:
            print("  BusId is NULL.")
