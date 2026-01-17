from models.MedicalAppointment import MedicalAppointment
from dtos.Doctor import Doctor
from sqlalchemy import select
from extensions import db
#It defines the method for getting appointment by doctor
def get_appointments_by_doctor(doctor:Doctor) -> list[MedicalAppointment]:
    #It declares medical appointment list
    doctor_medical_appointments : list[MedicalAppointment] = []
    #It gets medical appointments from database through ORM
    stmt = select(MedicalAppointment).where(MedicalAppointment.id_doctor==doctor.id_doctor)
    for row in db.session.execute(stmt):
        #It adds the Medical Appointment to the list
        doctor_medical_appointments.append(row.MedicalAppointment)
    #It returns the medical appointment list
    return doctor_medical_appointments
