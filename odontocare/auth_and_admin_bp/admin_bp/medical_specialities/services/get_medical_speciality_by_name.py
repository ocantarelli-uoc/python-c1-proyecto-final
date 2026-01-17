from models.MedicalSpeciality import MedicalSpeciality

#It defines the method for getting medical speciality by name
def get_medical_speciality_by_name(medical_speciality_name):
    #It gets the medical speciality from database through ORM
    medical_speciality = MedicalSpeciality.query.filter_by(name=medical_speciality_name).first()
    #It returns the gotten medical speciality
    return medical_speciality