from sqlalchemy import select
from sqlalchemy.orm import Session
from models.Patient import Patient
def list_patients() -> list[Patient]:
    patients : list[Patient] = []
    stmt = select(Patient)
    for row in Session.execute(stmt):
        patients.append(row.Patient)
    return patients
    