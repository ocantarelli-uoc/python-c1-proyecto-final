from models.MedicalAppointment import MedicalAppointment

#It defines the method for getting medical appointment by id
def get_medical_appointment_by_id(id) -> MedicalAppointment:
    #It gets the medical appointment from database through ORM
    medical_appointment = MedicalAppointment.query.get(id)
    #It returns the medical appointment
    return medical_appointment
