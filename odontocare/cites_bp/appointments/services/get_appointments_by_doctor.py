from models.MedicalAppointment import MedicalAppointment
from dtos.Doctor import Doctor
from sqlalchemy import select
from extensions import db
def get_appointments_by_doctor(doctor:Doctor) -> list[MedicalAppointment]:
    doctor_medical_appointments : list[MedicalAppointment] = []
    stmt = select(MedicalAppointment).where(MedicalAppointment.id_doctor==doctor.id_doctor)
    for row in db.session.execute(stmt):
        doctor_medical_appointments.append(row.MedicalAppointment)
    return doctor_medical_appointments
