import datetime
from models.MedicalAppointment import MedicalAppointment
from dtos.Doctor import Doctor
from sqlalchemy import select
from extensions import db
def get_appointments_by_date(date:datetime.datetime) -> list[MedicalAppointment]:
    medical_appointments : list[MedicalAppointment] = []
    stmt = select(MedicalAppointment).where( MedicalAppointment.appointment_date==date)
    for row in db.session.execute(stmt):
        medical_appointments.append(row.MedicalAppointment)
    return medical_appointments
