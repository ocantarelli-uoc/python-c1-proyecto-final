from models.Patient import Patient
#It defines the method for getting patient by id
def get_patient_by_name(name):
    #It gets the patient from database through ORM
    patient = Patient.query.filter_by(name=name).first()
     #It returns the gotten patient
    return patient