from flask import request
from models.Patient import Patient
from extensions import db
#It defines the method for creating a patient
def create_patient(user):
    try:
        #It get the request body in json format
        datos = request.get_json()
        #It gets the parameters from the body and it instances a patient from Patient class
        #to storing it to database through ORM
        patient = Patient(name=datos["name"],user=user,telephone=datos["telephone"])
        #It adds the patient to database through ORM
        db.session.add(patient)
        #It commit the changes
        db.session.commit()
    #It captures the generic exception
    except Exception as e:
        #It rollback the changes
        db.session.rollback()
        #It raise the generic exception above to the method which invoked this
        raise e
    #It returns the created patient
    return patient