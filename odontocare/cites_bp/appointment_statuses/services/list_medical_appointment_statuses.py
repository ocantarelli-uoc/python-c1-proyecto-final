from sqlalchemy import select
from extensions import db
from models.MedicalAppointmentStatus import MedicalAppointmentStatus
def list_medical_appointment_statuses() -> list[MedicalAppointmentStatus]:
    medical_appointment_statuses : list[MedicalAppointmentStatus] = []
    stmt = select(MedicalAppointmentStatus)
    for row in db.session.execute(stmt):
        medical_appointment_statuses.append(row.MedicalAppointmentStatus)
    return medical_appointment_statuses
    