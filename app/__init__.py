from flask import Flask
from .config import Config
from .models import db, tutor, alumno, materia  # Asegúrate de que todos los modelos están importados

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()  # Crea las tablas después de que todos los modelos están importados

    from .routes import init_routes
    init_routes(app)

    return app
