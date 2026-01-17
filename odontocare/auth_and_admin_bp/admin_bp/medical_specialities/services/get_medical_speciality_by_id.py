from models.MedicalSpeciality import MedicalSpeciality

#It defines the method for getting medical speciality by id
def get_medical_speciality_by_id(id):
    #It gets the medical speciality from database through ORM
    medical_speciality = MedicalSpeciality.query.get(id)
    #It returns the gotten medical speciality
    return medical_speciality