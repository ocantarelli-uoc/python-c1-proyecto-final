from models.Doctor import Doctor

def get_doctor_by_id(id):
    doctor = Doctor.query.get(id)
    return doctor