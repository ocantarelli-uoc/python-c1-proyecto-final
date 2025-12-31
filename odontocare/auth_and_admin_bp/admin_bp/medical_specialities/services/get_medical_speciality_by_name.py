from models.MedicalSpeciality import MedicalSpeciality

def get_medical_speciality_by_name(medical_speciality_name):
    medical_speciality = MedicalSpeciality.query.filter_by(name=medical_speciality_name).first()
    return medical_speciality