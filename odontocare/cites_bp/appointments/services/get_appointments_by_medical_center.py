from models.MedicalAppointment import MedicalAppointment
from dtos.MedicalCenter import MedicalCenter
from sqlalchemy import select
from extensions import db
#It defines the method for getting appointment by medical center
def get_appointments_by_medical_center(medical_center:MedicalCenter) -> list[MedicalAppointment]:
    #It declares medical appointment list
    center_medical_appointments : list[MedicalAppointment] = []
    #It gets medical appointments from database through ORM
    stmt = select(MedicalAppointment).where(MedicalAppointment.id_medical_center==medical_center.id_medical_center)
    for row in db.session.execute(stmt):
        #It adds the Medical Appointment to the list
        center_medical_appointments.append(row.MedicalAppointment)
    #It returns the medical appointment list
    return center_medical_appointments
