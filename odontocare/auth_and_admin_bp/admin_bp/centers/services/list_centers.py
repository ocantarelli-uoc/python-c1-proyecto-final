from sqlalchemy import select
from extensions import db
from models.MedicalCenter import MedicalCenter
#It defines the method for listing medical centers
def list_centers() -> list[MedicalCenter]:
    #It declares the variable for adding the medical centers gotten
    #from database through ORM
    centers : list[MedicalCenter] = []
    #It selects the medical centers from database through ORM
    stmt = select(MedicalCenter)
    #for every medical center gotten from database
    for row in db.session.execute(stmt):
        #It adds the current medical center to the list
        centers.append(row.MedicalCenter)
    #It returns the medical center list gotten from database
    #through ORM
    return centers