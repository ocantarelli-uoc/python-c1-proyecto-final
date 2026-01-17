from models.MedicalCenter import MedicalCenter
#It defines the method for getting medical center by id
def get_medical_center_by_id(id):
    #It gets the medical center from database through ORM
    medical_center = MedicalCenter.query.get(id)
    #It returns the gotten medical center
    return medical_center