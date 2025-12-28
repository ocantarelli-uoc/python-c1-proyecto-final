from flask import Flask
from odontocare.auth_and_admin_bp import auth_bp

def create_app():
    app = Flask(__name__)

    # Registramos el Blueprint de auth
    app.register_blueprint(auth_bp, url_prefix='/api/v1')
    
    return app