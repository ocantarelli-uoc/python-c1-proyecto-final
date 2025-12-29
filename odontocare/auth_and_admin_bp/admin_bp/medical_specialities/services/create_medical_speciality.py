from flask import request
from models.MedicalSpeciality import MedicalSpeciality
from extensions import db

def create_medical_speciality():
    datos = request.get_json()
    created_medical_speciality = MedicalSpeciality(name=datos["medical_speciality_name"])
    db.session.add(created_medical_speciality)
    db.session.commit()
    return created_medical_speciality