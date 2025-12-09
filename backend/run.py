from app import create_app

# Creamos la aplicación
app = create_app()

if __name__ == '__main__':
    # Ejecutamos el servidor en el puerto 5000
    # debug=True permite que el servidor se reinicie si cambias código
    # Trigger reload
    app.run(debug=True)