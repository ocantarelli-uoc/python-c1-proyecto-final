from models.Doctor import Doctor

#It defines the method for getting doctor by name
def get_doctor_by_name(name):
    #It gets the doctor from database through ORM
    doctor = Doctor.query.filter_by(name=name).first()
    #It returns the gotten doctor
    return doctor