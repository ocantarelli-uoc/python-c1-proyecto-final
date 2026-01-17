import datetime
from models.MedicalAppointment import MedicalAppointment
from sqlalchemy import select
from extensions import db
#It defines the method for getting appointment by date
def get_appointments_by_date(date:datetime.datetime) -> list[MedicalAppointment]:
    #It declares medical appointment list
    medical_appointments : list[MedicalAppointment] = []
    #It gets medical appointments from database through ORM
    stmt = select(MedicalAppointment).where( MedicalAppointment.appointment_date==date)
    for row in db.session.execute(stmt):
        #It adds the Medical Appointment to the list
        medical_appointments.append(row.MedicalAppointment)
    #It returns the medical appointment list
    return medical_appointments
