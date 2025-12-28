from flask import Flask
from odontocare.auth_and_admin_bp.auth_bp.recursos import auth
from odontocare.auth_and_admin_bp.admin_bp.patients.recursos import patients
from odontocare.auth_and_admin_bp.admin_bp.doctors.recursos import doctors
from odontocare.auth_and_admin_bp.admin_bp.centers.recursos import centers



def create_app():
    app = Flask(__name__)

    # Registramos el Blueprint de auth
    app.register_blueprint(auth, url_prefix='/api/v1')
    # Registramos el Blueprint de patients
    app.register_blueprint(patients, url_prefix='/api/v1')
    # Registramos el Blueprint de doctors
    app.register_blueprint(doctors, url_prefix='/api/v1')
    # Registramos el Blueprint de centers
    app.register_blueprint(centers, url_prefix='/api/v1')
    
    return app