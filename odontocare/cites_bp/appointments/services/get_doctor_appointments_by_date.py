import datetime
from models.MedicalAppointment import MedicalAppointment
from dtos.Doctor import Doctor
from sqlalchemy import select
from extensions import db
#It defines the method for getting doctor appointments by date
def get_doctor_appointments_by_date(doctor:Doctor,date:datetime.datetime) -> list[MedicalAppointment]:
    #It declares medical appointment list
    doctor_medical_appointments : list[MedicalAppointment] = []
    #It gets medical appointments from database through ORM
    stmt = select(MedicalAppointment).where(MedicalAppointment.id_doctor==doctor.id_doctor,
                                            MedicalAppointment.appointment_date==date)
    for row in db.session.execute(stmt):
        #It adds the Medical Appointment to the list
        doctor_medical_appointments.append(row.MedicalAppointment)
    #It returns the doctor medical appointment list
    return doctor_medical_appointments
