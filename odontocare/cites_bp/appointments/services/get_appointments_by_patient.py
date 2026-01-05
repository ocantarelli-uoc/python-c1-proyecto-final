from models.MedicalAppointment import MedicalAppointment
from dtos.Patient import Patient
from sqlalchemy import select
from extensions import db
def get_appointments_by_patient(patient:Patient) -> list[MedicalAppointment]:
    patient_medical_appointments : list[MedicalAppointment] = []
    stmt = select(MedicalAppointment).where(MedicalAppointment.id_patient==patient.id_patient)
    for row in db.session.execute(stmt):
        patient_medical_appointments.append(row.MedicalAppointment)
    return patient_medical_appointments
