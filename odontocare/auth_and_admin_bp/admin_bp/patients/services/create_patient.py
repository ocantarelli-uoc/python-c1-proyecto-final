from flask import request
from models.Patient import Patient
from extensions import db

def create_patient(user_id):
    datos = request.get_json()
    patient = Patient(name=datos["name"],id_user=user_id,telephone=datos["telephone"])
    db.session.add(patient)
    db.session.commit()
    return patient