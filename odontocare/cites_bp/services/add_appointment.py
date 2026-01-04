import datetime
from zoneinfo import ZoneInfo
from extensions import db
from dtos.Doctor import Doctor
from dtos.Patient import Patient
from dtos.MedicalCenter import MedicalCenter
from models.MedicalAppointment import MedicalAppointment
from models.MedicalAppointmentStatus import MedicalAppointmentStatus
from services.get_doctor_appointments_by_date import get_doctor_appointments_by_date
from services.get_doctor_by_id import get_doctor_by_id
from services.get_patient_by_id import get_patient_by_id
from services.get_medical_center_by_id import get_medical_center_by_id
from exceptions.not_found.DoctorNotFoundException import DoctorNotFoundException
from exceptions.not_found.PatientNotFoundException import PatientNotFoundException
from exceptions.not_found.MedicalCenterNotFoundException import MedicalCenterNotFoundException
from exceptions.not_found.MedicalAppointmentStatusNotFoundException import MedicalAppointmentStatusNotFoundException
from exceptions.already_exists.MedicalAppointmentAlreadyExistsException import MedicalAppointmentAlreadyExistsException

def add_appointment(appointment_input_dict:dict):
    try:
        doctor : Doctor = get_doctor_by_id(int(appointment_input_dict['id_doctor']))
        if doctor is None:
            raise DoctorNotFoundException()
        patient : Patient = get_patient_by_id(int(appointment_input_dict['id_patient']))
        if patient is None:
            raise PatientNotFoundException()
        medical_center : MedicalCenter = get_medical_center_by_id(int(appointment_input_dict['id_medical_center']))
        if medical_center is None:
            raise MedicalCenterNotFoundException()

        doctor_medical_appointments : list[MedicalAppointment] = get_doctor_appointments_by_date(doctor,
        datetime.datetime.fromisoformat(appointment_input_dict['appointment_date']).astimezone(ZoneInfo("Europe/Madrid")))
        if doctor_medical_appointments is not None and len(doctor_medical_appointments) >= 1:
            raise MedicalAppointmentAlreadyExistsException()

        medical_appointment_status:MedicalAppointmentStatus = MedicalAppointmentStatus.query.filter_by(name=appointment_input_dict['status']).first()
        if medical_appointment_status is None:
            raise MedicalAppointmentStatusNotFoundException()
        medical_appointment : MedicalAppointment = MedicalAppointment(appointment_date=datetime.datetime.fromisoformat(appointment_input_dict['appointment_date']).astimezone(ZoneInfo("Europe/Madrid")),
                motiu=appointment_input_dict['motiu'],
                id_doctor=appointment_input_dict['id_doctor'],
                id_medical_centre=appointment_input_dict['id_medical_centre'],
                id_patient=appointment_input_dict['id_patient'],
                id_action_user=appointment_input_dict['id_action_user'],
                medical_appointment_status=medical_appointment_status
        )
        db.session.add(medical_appointment)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
