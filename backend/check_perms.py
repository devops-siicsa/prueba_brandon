from app import create_app, db
from app.models.auth_models import Permiso

app = create_app()

def check_perms():
    with app.app_context():
        print("Buscando permiso 'catalogs:view'...")
        perm = Permiso.query.filter_by(Codigo='catalogs:view').first()
        if perm:
            print(f"Encontrado: {perm.Codigo} - {perm.Descripcion}")
        else:
            print("NO ENCONTRADO 'catalogs:view'")
            
        print("Buscando permiso 'catalogs:create'...")
        perm = Permiso.query.filter_by(Codigo='catalogs:create').first()
        if perm:
            print(f"Encontrado: {perm.Codigo} - {perm.Descripcion}")
        else:
            print("NO ENCONTRADO 'catalogs:create'")

if __name__ == '__main__':
    check_perms()
