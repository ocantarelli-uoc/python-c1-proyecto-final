from models.Patient import Patient

#It defines the method for getting patient by id
def get_patient_by_id(id):
    #It gets the patient from database through ORM
    patient = Patient.query.get(id)
    #It returns the gotten patient
    return patient