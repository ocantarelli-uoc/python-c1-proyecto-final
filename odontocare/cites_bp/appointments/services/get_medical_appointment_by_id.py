from models.MedicalAppointment import MedicalAppointment

def get_medical_appointment_by_id(id):
    medical_appointment = MedicalAppointment.query.get(id)
    return medical_appointment
