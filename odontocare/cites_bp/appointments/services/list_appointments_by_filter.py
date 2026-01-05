from flask import Blueprint, jsonify, request
import datetime
from decorators.require_role import require_role
from dtos.User import User
from models.MedicalAppointment import MedicalAppointment
from enums.MedicalAppointmentStatusEnum import MedicalAppointmentStatusEnum
from appointments.services.get_doctor_by_id import get_doctor_by_id as orm_get_doctor_by_id
from appointments.services.get_appointments_by_patient import get_appointments_by_patient
from appointments.services.get_patient_by_id import get_patient_by_id as orm_get_patient_by_id
from dtos.Doctor import Doctor
from appointments.services.get_appointments_by_doctor import get_appointments_by_doctor
from dtos.Patient import Patient
from appointments.services.get_appointments_by_patient import get_appointments_by_patient
from dtos.MedicalCenter import MedicalCenter
from appointments.services.get_medical_center_by_id import get_medical_center_by_id as orm_get_medical_center_by_id
from appointments.services.get_appointments_by_medical_center import get_appointments_by_medical_center as get_appointments_by_medical_center
from models.MedicalAppointmentStatus import MedicalAppointmentStatus
from appointment_statuses.services.get_medical_appointment_status_by_id import get_medical_appointment_status_by_id as orm_get_medical_appointment_status_by_id
from appointments.services.get_appointments_by_status import get_appointments_by_status
from appointments.services.get_appointments_by_date import get_appointments_by_date
def list_appointments_by_filter(filter_dict,*args,**kwargs):
    authorized_user : User = kwargs.get('authorized_user')
    appointments = []
    filter_by = filter_dict["filter_by"]
    filter_value = filter_dict["filter_value"]
    if filter_by == "doctor":
        require_role(required_roles=["admin","doctor"])
        if authorized_user.user_role.name=="doctor":
            doctor_id = authorized_user.id_user
        else:
         doctor_id = filter_value
        doctor : Doctor = orm_get_doctor_by_id(doctor_id)
        if doctor is not None:
            appointments : list[MedicalAppointment] = get_appointments_by_doctor(doctor)
    if filter_by == "patient":
        require_role(required_roles=["admin"])
        patient : Patient = orm_get_patient_by_id(filter_value)
        if patient is not None:
            appointments : list[MedicalAppointment] = get_appointments_by_patient(
                patient
            )
    if filter_by == "center":
        require_role(required_roles=["admin"])
        medical_center : MedicalCenter = orm_get_medical_center_by_id(filter_value)
        if medical_center is not None:
            appointments : list[MedicalAppointment] = get_appointments_by_medical_center(
                medical_center
            )
    if filter_by == "status":
        require_role(required_roles=["admin"])
        medical_status : MedicalAppointmentStatus = orm_get_medical_appointment_status_by_id(filter_value)
        if medical_status is not None:
            appointments : list[MedicalAppointment] = get_appointments_by_status(
                medical_status
            )
    if filter_by == "date":
        require_role(required_roles=["admin","secretary"])
        if filter_value is not None:
            appointments : list[MedicalAppointment] = get_appointments_by_date(
            datetime.datetime.fromisoformat(str(filter_value)))
    return appointments