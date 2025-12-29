from models.Patient import Patient

def get_patient_by_id(id):
    patient = Patient.query.get(id)
    return patient