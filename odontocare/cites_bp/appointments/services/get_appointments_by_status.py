from models.MedicalAppointment import MedicalAppointment
from models.MedicalAppointmentStatus import MedicalAppointmentStatus
from sqlalchemy import select
from extensions import db
def get_appointments_by_status(medical_appointment_status:MedicalAppointmentStatus) -> list[MedicalAppointment]:
    medical_appointments : list[MedicalAppointment] = []
    stmt = select(MedicalAppointment).where(MedicalAppointment.id_medical_status==medical_appointment_status.id_medical_status)
    for row in db.session.execute(stmt):
        medical_appointments.append(row.MedicalAppointment)
    return medical_appointments
