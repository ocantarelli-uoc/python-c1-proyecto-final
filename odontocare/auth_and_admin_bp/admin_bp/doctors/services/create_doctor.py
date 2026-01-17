from flask import request
from models.Doctor import Doctor
from models.MedicalSpeciality import MedicalSpeciality
from extensions import db
#It defines the method for creating a doctor
def create_doctor(user):
    try:
        #It get the request body in json format
        datos = request.get_json()
        #It gets the medical speciality by name
        medical_speciality:MedicalSpeciality = MedicalSpeciality.query.filter_by(name=datos["medical_speciality"]).first()
        #It gets the parameters from the body and it instances a doctor from Doctor class
        #to storing it to database through ORM
        doctor = Doctor(name=datos["name"],user=user,medical_speciality=medical_speciality)
        #It adds the doctor to database through ORM
        db.session.add(doctor)
        #It commit the changes
        db.session.commit()
    #It captures the generic exception
    except Exception as e:
        #It rollback the changes
        db.session.rollback()
        #It raise the generic exception above to the method which invoked this
        raise e
    #It returns the created doctor
    return doctor