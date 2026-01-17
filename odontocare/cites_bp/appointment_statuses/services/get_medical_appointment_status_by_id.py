from models.MedicalAppointmentStatus import MedicalAppointmentStatus

#It defines the method for getting medical appointment status by id
def get_medical_appointment_status_by_id(id) -> MedicalAppointmentStatus:
    #It gets the medical appointment status by id from database through ORM
    medical_appointment_status = MedicalAppointmentStatus.query.get(id)
    #It returns the medical appointment status get by id from database through ORM
    return medical_appointment_status
