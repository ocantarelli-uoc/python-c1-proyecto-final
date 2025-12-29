from models.MedicalSpeciality import MedicalSpeciality

def get_medical_speciality_by_id(id):
    medical_speciality = MedicalSpeciality.query.get(id)
    return medical_speciality