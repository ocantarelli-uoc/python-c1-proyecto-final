from extensions import db
from models.MedicalAppointmentStatus import MedicalAppointmentStatus
from exceptions.already_exists.MedicalAppointmentStatusAlreadyExistsException import MedicalAppointmentStatusAlreadyExistsException
#It defines the method for creating appointment status
def create_medical_appointment_status(medical_appointment_dict) -> MedicalAppointmentStatus:
    try:
        #It tries to get medical appointment status by name
        medical_appointment_status:MedicalAppointmentStatus = MedicalAppointmentStatus.query.filter_by(name=medical_appointment_dict['status_name']).first()
        #It checks if medical appointment status is not None (null)
        if medical_appointment_status is not None:
            #It throws medical appointment status already exists
            raise MedicalAppointmentStatusAlreadyExistsException()
        #It instances the medical appointment status object for adding to database through ORM
        medical_appointment_status : MedicalAppointmentStatus = MedicalAppointmentStatus(
            name=medical_appointment_dict['status_name']
        )
        #It saves medical appointment status to database through ORM
        db.session.add(medical_appointment_status)
        #It commit the changes to database
        db.session.commit()
        #It returns the created medical appointment status
        return medical_appointment_status
    #It captures the generic exception
    except Exception as e:
        #It rollback the changes
        db.session.rollback()
        #It raise the generic exception above to the invoking method
        raise e