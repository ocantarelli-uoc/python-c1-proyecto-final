from extensions import db
from models.MedicalAppointmentStatus import MedicalAppointmentStatus
from exceptions.already_exists.MedicalAppointmentStatusAlreadyExistsException import MedicalAppointmentStatusAlreadyExistsException
def create_medical_appointment_status(medical_appointment_dict) -> MedicalAppointmentStatus:
    try:
        medical_appointment_status:MedicalAppointmentStatus = MedicalAppointmentStatus.query.filter_by(name=medical_appointment_dict['status_name']).first()
        if medical_appointment_status is not None:
            raise MedicalAppointmentStatusAlreadyExistsException()
        medical_appointment_status : MedicalAppointmentStatus = MedicalAppointmentStatus(
            name=medical_appointment_dict['status_name']
        )
        db.session.add(medical_appointment_status)
        db.session.commit()
        return medical_appointment_status
    except Exception as e:
        db.session.rollback()
        raise e