from flask import Flask
from sqlalchemy.pool import StaticPool
from extensions import db
from appointments.recursos.cites import cites_bp
from appointment_statuses.recursos.appointment_statuses import appointment_statuses_bp

def create_app():
    app = Flask(__name__)

    # Registramos el Blueprint de cites
    app.register_blueprint(cites_bp, url_prefix='/api/v1')

    # Registramos el Blueprint de appointment_statuses_bp
    app.register_blueprint(appointment_statuses_bp, url_prefix='/api/v1')

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