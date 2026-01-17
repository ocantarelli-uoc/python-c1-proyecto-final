from flask import request
from models.MedicalSpeciality import MedicalSpeciality
from extensions import db
#It defines the method for creating a medical speciality
def create_medical_speciality():
    try:
        #It get the request body in json format
        datos = request.get_json()
        #It gets the parameters from the body and it instances an medical speciality from MedicalSpeciality class
        #to storing it to database through ORM
        created_medical_speciality = MedicalSpeciality(name=datos["medical_speciality_name"])
        #It adds the medical speciality to database through ORM
        db.session.add(created_medical_speciality)
        #It commit the changes
        db.session.commit()
    #It captures the generic exception
    except Exception as e:
        #It rollback the changes
        db.session.rollback()
        #It raise the generic exception above to the method which invoked this
        raise e
    #It returns the created medical speciality
    return created_medical_speciality