from models.MedicalCenter import MedicalCenter
#It defines the method for getting medical center by name
def get_center_by_name(name):
    #It gets the medical center from database through ORM
    medical_center = MedicalCenter.query.filter_by(name=name).first()
    #It returns the gotten medical center
    return medical_center