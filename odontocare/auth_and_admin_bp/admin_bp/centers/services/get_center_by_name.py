from models.MedicalCenter import MedicalCenter

def get_center_by_name(name):
    medical_center = MedicalCenter.query.filter_by(name=name).first()
    return medical_center