from models.MedicalCenter import MedicalCenter

def get_medical_center_by_id(id):
    medical_center = MedicalCenter.query.get(id)
    return medical_center