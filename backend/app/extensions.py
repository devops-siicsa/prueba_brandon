from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Inicializamos la base de datos (sin vincularla a la app todavía)
db = SQLAlchemy()

# Inicializamos CORS (Para que el Frontend Vue pueda hablar con este Backend)
cors = CORS()