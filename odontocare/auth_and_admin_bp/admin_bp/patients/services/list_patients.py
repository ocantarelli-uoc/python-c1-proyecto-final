from sqlalchemy import select
from extensions import db
from models.Patient import Patient
#It defines the method for listing patients
def list_patients() -> list[Patient]:
    #It declares the variable for adding the patients gotten
    #from database through ORM
    patients : list[Patient] = []
    #It selects the patients from database through ORM
    stmt = select(Patient)
    #for every patient gotten from database
    for row in db.session.execute(stmt):
        #It adds the current patient to the list
        patients.append(row.Patient)
    #It returns the patient list gotten from database
    #through ORM
    return patients
    