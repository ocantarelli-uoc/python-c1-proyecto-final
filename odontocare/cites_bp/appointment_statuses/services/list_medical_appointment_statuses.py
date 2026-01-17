from sqlalchemy import select
from extensions import db
from models.MedicalAppointmentStatus import MedicalAppointmentStatus
#It defines the method for listing medical appointment statuses
def list_medical_appointment_statuses() -> list[MedicalAppointmentStatus]:
    #It declares the variable for adding the medical appointment statuses gotten
    #from database through ORM
    medical_appointment_statuses : list[MedicalAppointmentStatus] = []
    #It selects the medical appointment statuses from database through ORM
    stmt = select(MedicalAppointmentStatus)
    #for every medical appointment status gotten from database
    for row in db.session.execute(stmt):
        #It adds the current medical appointment status to the list
        medical_appointment_statuses.append(row.MedicalAppointmentStatus)
    #It returns the medical appointment statuses list gotten from database
    #through ORM
    return medical_appointment_statuses
    