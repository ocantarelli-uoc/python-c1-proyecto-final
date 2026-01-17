from models.MedicalAppointment import MedicalAppointment
from dtos.Patient import Patient
from sqlalchemy import select
from extensions import db
#It defines the method for getting appointment by patient
def get_appointments_by_patient(patient:Patient) -> list[MedicalAppointment]:
    #It declares medical appointment list
    patient_medical_appointments : list[MedicalAppointment] = []
    #It gets medical appointments from database through ORM
    stmt = select(MedicalAppointment).where(MedicalAppointment.id_patient==patient.id_patient)
    for row in db.session.execute(stmt):
        #It adds the Medical Appointment to the list
        patient_medical_appointments.append(row.MedicalAppointment)
    #It returns the medical appointment list
    return patient_medical_appointments
