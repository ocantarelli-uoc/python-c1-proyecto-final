from flask import Flask
from sqlalchemy.pool import StaticPool
from extensions import db
from auth_bp.recursos.auth import auth_bp
from admin_bp.users.recursos.users import users_bp
from admin_bp.patients.recursos.patients import patients_bp
from admin_bp.doctors.recursos.doctors import doctors_bp
from admin_bp.centers.recursos.centers import centers_bp
from admin_bp.user_roles.recursos.user_roles import users_roles_bp
from admin_bp.medical_specialities.recursos.medical_specialities import medical_specialities_bp

def create_app():
    app = Flask(__name__)
    # Registramos el Blueprint de auth
    app.register_blueprint(auth_bp, url_prefix='/api/v1')
    # Registramos el Blueprint de users
    app.register_blueprint(users_bp, url_prefix='/api/v1')
    # Registramos el Blueprint de patients
    app.register_blueprint(patients_bp, url_prefix='/api/v1')
    # Registramos el Blueprint de doctors
    app.register_blueprint(doctors_bp, url_prefix='/api/v1')
    # Registramos el Blueprint de centers
    app.register_blueprint(centers_bp, url_prefix='/api/v1')
    # Registramos el Blueprint de roles de usuarios
    app.register_blueprint(users_roles_bp, url_prefix='/api/v1')
    # Registramos el Blueprint de roles de especialidades médicas
    app.register_blueprint(medical_specialities_bp, url_prefix='/api/v1')

     # BD en memoria compartida durante la vida de la app
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "connect_args": {"check_same_thread": False},
        "poolclass": StaticPool
    }
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app