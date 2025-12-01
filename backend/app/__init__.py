from flask import Flask, jsonify
from app.config import Config
from app.extensions import db, cors
from sqlalchemy import text

def create_app(config_class=Config):
    """
    Función Factory: Crea y configura una instancia de la aplicación Flask.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializar extensiones con la app creada
    db.init_app(app)
    
    # Permitir CORS para localhost y dominios de ngrok
    cors.init_app(app, resources={r"/api/*": {"origins": [
        "http://localhost:3000",
        r"https://.*\.ngrok-free\.dev"
    ]}}, supports_credentials=True)

    # Registrar Blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.config_routes import config_bp
    from app.routes.audit_routes import audit_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(config_bp)
    app.register_blueprint(audit_bp)

    # Registrar Hooks de Auditoría
    from app.audit_hooks import register_audit_hooks
    register_audit_hooks(app)

    # Crear tablas si no existen (con manejo de errores para no bloquear inicio)
    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print(f"Error creating tables: {e}")

    # --- RUTA DE PRUEBA (HEALTH CHECK) ---
    @app.route('/health', methods=['GET'])
    def health_check():
        try:
            # Intenta hacer una consulta simple 'SELECT 1' a la BD
            # Usamos text() para que SQLAlchemy sepa que es SQL puro
            db.session.execute(text('SELECT 1'))
            return jsonify({
                "status": "success", 
                "message": "Sistema de Inventario Backend Corriendo", 
                "database": "Conectada Exitosamente"
            }), 200
        except Exception as e:
            return jsonify({
                "status": "error", 
                "message": "Error de conexión a Base de Datos", 
                "error_detail": str(e)
            }), 500

    return app