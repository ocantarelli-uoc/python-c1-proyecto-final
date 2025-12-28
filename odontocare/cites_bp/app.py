from flask import Flask
from odontocare import cites_bp

def create_app():
    app = Flask(__name__)

    # Registramos el Blueprint de cites
    app.register_blueprint(cites_bp, url_prefix='/api/v1')
    
    return app