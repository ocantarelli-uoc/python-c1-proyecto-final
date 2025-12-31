from models.Doctor import Doctor

def get_doctor_by_name(name):
    doctor = Doctor.query.filter_by(name=name).first()
    return doctor