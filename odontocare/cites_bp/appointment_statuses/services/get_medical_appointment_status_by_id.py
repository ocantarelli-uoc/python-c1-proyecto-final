from models.MedicalAppointmentStatus import MedicalAppointmentStatus

def get_medical_appointment_status_by_id(id) -> MedicalAppointmentStatus:
    medical_appointment_status = MedicalAppointmentStatus.query.get(id)
    return medical_appointment_status
