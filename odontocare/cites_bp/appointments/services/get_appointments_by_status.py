from models.MedicalAppointment import MedicalAppointment
from models.MedicalAppointmentStatus import MedicalAppointmentStatus
from sqlalchemy import select
from extensions import db
#It defines the method for getting appointment by status
def get_appointments_by_status(medical_appointment_status:MedicalAppointmentStatus) -> list[MedicalAppointment]:
    #It declares medical appointment list
    medical_appointments : list[MedicalAppointment] = []
    #It gets medical appointments from database through ORM
    stmt = select(MedicalAppointment).where(MedicalAppointment.id_medical_status==medical_appointment_status.id_medical_status)
    for row in db.session.execute(stmt):
        #It adds the Medical Appointment to the list
        medical_appointments.append(row.MedicalAppointment)
    #It returns the medical appointment list
    return medical_appointments
