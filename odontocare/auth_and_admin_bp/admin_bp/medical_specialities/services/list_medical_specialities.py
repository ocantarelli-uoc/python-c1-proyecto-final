from sqlalchemy import select
from extensions import db
from models.MedicalSpeciality import MedicalSpeciality
#It defines the method for listing medical specialities
def list_medical_specialities() -> list[MedicalSpeciality]:
    #It declares the variable for adding the medical specialities gotten
    #from database through ORM
    medical_specialities : list[MedicalSpeciality] = []
    #It selects the medical specialities from database through ORM
    stmt = select(MedicalSpeciality)
    #for every medical speciality gotten from database
    for row in db.session.execute(stmt):
        #It adds the current medical speciality to the list
        medical_specialities.append(row.MedicalSpeciality)
    #It returns the medical speciality list gotten from database
    #through ORM
    return medical_specialities