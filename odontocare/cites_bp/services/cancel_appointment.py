import datetime
from extensions import db
from dtos.Doctor import Doctor
from dtos.Patient import Patient
from dtos.MedicalCenter import MedicalCenter
from models.MedicalAppointment import MedicalAppointment
from models.MedicalAppointmentStatus import MedicalAppointmentStatus
from services.get_doctor_appointments_by_date import get_doctor_appointments_by_date
from services.get_doctor_by_id import get_doctor_by_id
from services.get_patient_by_id import get_patient_by_id
from exceptions.not_found.DoctorNotFoundException import DoctorNotFoundException
from exceptions.not_found.PatientNotFoundException import PatientNotFoundException
from exceptions.not_found.MedicalCenterNotFoundException import MedicalCenterNotFoundException
from exceptions.not_found.MedicalAppointmentStatusNotFoundException import MedicalAppointmentStatusNotFoundException
from exceptions.already_exists.MedicalAppointmentAlreadyExistsException import MedicalAppointmentAlreadyExistsException

def modify_appointment_status(id,action):
    try:
        if action == "activate":
            status = "pending"
        if action == "cancel":
            status = "cancelled"
        medical_appointment:MedicalAppointment = MedicalAppointment.query.filter_by(id=id).first()
        medical_appointment_status:MedicalAppointmentStatus = MedicalAppointmentStatus.query.filter_by(name=status).first()
        if medical_appointment_status is None:
            raise MedicalAppointmentStatusNotFoundException()
        medical_appointment.medical_appointment_status = medical_appointment_status
        db.session.add(medical_appointment)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
