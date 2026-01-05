from models.MedicalAppointment import MedicalAppointment
from dtos.MedicalCenter import MedicalCenter
from sqlalchemy import select
from extensions import db
def get_appointments_by_medical_center(medical_center:MedicalCenter) -> list[MedicalAppointment]:
    center_medical_appointments : list[MedicalAppointment] = []
    stmt = select(MedicalAppointment).where(MedicalAppointment.id_medical_center==medical_center.id_medical_center)
    for row in db.session.execute(stmt):
        center_medical_appointments.append(row.MedicalAppointment)
    return center_medical_appointments
