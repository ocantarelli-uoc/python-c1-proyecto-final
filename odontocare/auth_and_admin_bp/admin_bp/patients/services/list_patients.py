from sqlalchemy import select
from extensions import db
from models.Patient import Patient
def list_patients() -> list[Patient]:
    patients : list[Patient] = []
    stmt = select(Patient)
    for row in db.session.execute(stmt):
        patients.append(row.Patient)
    return patients
    