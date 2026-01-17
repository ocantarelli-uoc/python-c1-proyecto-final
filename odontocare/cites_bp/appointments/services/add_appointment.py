import datetime
from extensions import db
from dtos.Doctor import Doctor
from dtos.Patient import Patient
from dtos.MedicalCenter import MedicalCenter
from models.MedicalAppointment import MedicalAppointment
from models.MedicalAppointmentStatus import MedicalAppointmentStatus
from appointments.services.get_doctor_appointments_by_date import get_doctor_appointments_by_date
from appointments.services.get_doctor_by_id import get_doctor_by_id
from appointments.services.get_patient_by_id import get_patient_by_id
from appointments.services.get_medical_center_by_id import get_medical_center_by_id
from exceptions.not_found.DoctorNotFoundException import DoctorNotFoundException
from exceptions.not_found.PatientNotFoundException import PatientNotFoundException
from exceptions.not_found.MedicalCenterNotFoundException import MedicalCenterNotFoundException
from exceptions.not_found.MedicalAppointmentStatusNotFoundException import MedicalAppointmentStatusNotFoundException
from exceptions.already_exists.MedicalAppointmentAlreadyExistsException import MedicalAppointmentAlreadyExistsException

#It defines the method for adding a medical appointment
def add_appointment(appointment_input_dict:dict):
    try:
        #It gets doctor by id
        doctor : Doctor = get_doctor_by_id(int(appointment_input_dict['id_doctor']))
        #It checks if doctor is None
        if doctor is None:
            #If doctor is None,it throws a doctor not found exception
            raise DoctorNotFoundException()
        #It gets patient by id
        patient : Patient = get_patient_by_id(int(appointment_input_dict['id_patient']))
        #It checks if patient is None
        if patient is None:
            #If patient is None, it throws a patient not found exception
            raise PatientNotFoundException()
        #It gets medical center by id
        medical_center : MedicalCenter = get_medical_center_by_id(int(appointment_input_dict['id_medical_center']))
        #It checks if medical center is None
        if medical_center is None:
            #It medical_center is None, it throws a medical center not found exception
            raise MedicalCenterNotFoundException()
        #It gets medical appointments by date
        doctor_medical_appointments : list[MedicalAppointment] = get_doctor_appointments_by_date(doctor,
        datetime.datetime.fromisoformat(str(appointment_input_dict['appointment_date'])))
        #If the doctor has already a medical appointment for this date, it throws a medical appointment already exists exception
        if doctor_medical_appointments is not None and len(doctor_medical_appointments) >= 1:
            raise MedicalAppointmentAlreadyExistsException()
        #It gets the medical appointment status object from database through ORM
        medical_appointment_status:MedicalAppointmentStatus = MedicalAppointmentStatus.query.filter_by(name=appointment_input_dict['status']).first()
        #If medical appointment status is none, it throws a medical appointment status not found exception
        if medical_appointment_status is None:
            raise MedicalAppointmentStatusNotFoundException()
        #It instances an object of MedicalAppointment with the data of medical appointment to be added
        medical_appointment : MedicalAppointment = MedicalAppointment(appointment_date=datetime.datetime.fromisoformat(str(appointment_input_dict['appointment_date'])),
                motiu=appointment_input_dict['motiu'],
                id_doctor=appointment_input_dict['id_doctor'],
                id_medical_center=appointment_input_dict['id_medical_center'],
                id_patient=appointment_input_dict['id_patient'],
                id_action_user=appointment_input_dict['id_action_user'],
                medical_appointment_status=medical_appointment_status
        )
        #It add the medical appointment to database through ORM
        db.session.add(medical_appointment)
        #It commits the changes
        db.session.commit()
        #It returns the created medical appointment
        return medical_appointment
    #It captures the generic exception
    except Exception as e:
        #It rollbacks the changes
        db.session.rollback()
        #It throws the exception above (to invoking method)
        raise e
