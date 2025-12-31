from models.Patient import Patient

def get_patient_by_name(name):
    patient = Patient.query.filter_by(name=name).first()
    return patient