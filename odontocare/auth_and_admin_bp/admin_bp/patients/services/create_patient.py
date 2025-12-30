from flask import request
from models.Patient import Patient
from extensions import db

def create_patient(user):
    datos = request.get_json()
    patient = Patient(name=datos["name"],user=user,telephone=datos["telephone"])
    db.session.add(patient)
    db.session.commit()
    return patient