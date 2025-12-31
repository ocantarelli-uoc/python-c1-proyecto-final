from flask import request
from models.Doctor import Doctor
from models.MedicalSpeciality import MedicalSpeciality
from extensions import db

def create_doctor(user):
    try:
        datos = request.get_json()
        medical_speciality:MedicalSpeciality = MedicalSpeciality.query.filter_by(name=datos["medical_speciality"]).first()
        doctor = Doctor(name=datos["name"],user=user,medical_speciality=medical_speciality)
        db.session.add(doctor)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    return doctor