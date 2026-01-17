from sqlalchemy import select
from extensions import db
from models.Doctor import Doctor
#It defines the method for listing doctors
def list_doctors() -> list[Doctor]:
    #It declares the variable for adding the doctors gotten
    #from database through ORM
    doctors : list[Doctor] = []
    #It selects the doctors from database through ORM
    stmt = select(Doctor)
    #for every doctor gotten from database
    for row in db.session.execute(stmt):
        #It adds the current doctor to the list
        doctors.append(row.Doctor)
    #It returns the doctor list gotten from database
    #through ORM
    return doctors