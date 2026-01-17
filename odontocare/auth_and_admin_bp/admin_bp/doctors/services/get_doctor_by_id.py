from models.Doctor import Doctor

#It defines the method for getting doctor by id
def get_doctor_by_id(id):
    #It gets the doctor from database through ORM
    doctor = Doctor.query.get(id)
    #It returns the gotten doctor
    return doctor