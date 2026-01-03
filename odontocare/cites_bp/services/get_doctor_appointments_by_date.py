import datetime
from models.MedicalAppointment import MedicalAppointment
from dtos.Doctor import Doctor
from sqlalchemy import select
from extensions import db
def get_doctor_appointments_by_date(doctor:Doctor,date:datetime) -> list[MedicalAppointment]:
    doctor_medical_appointments : list[MedicalAppointment] = []
    stmt = select(MedicalAppointment).where(MedicalAppointment.id_doctor==doctor.id_doctor,MedicalAppointment.appointment_date==date)
    for row in db.session.execute(stmt):
        doctor_medical_appointments.append(row.MedicalAppointment)
    return doctor_medical_appointments