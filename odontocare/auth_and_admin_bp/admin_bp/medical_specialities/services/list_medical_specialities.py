from sqlalchemy import select
from extensions import db
from models.MedicalSpeciality import MedicalSpeciality
def list_medical_specialities() -> list[MedicalSpeciality]:
    medical_specialities : list[MedicalSpeciality] = []
    stmt = select(MedicalSpeciality)
    for row in db.session.execute(stmt):
        medical_specialities.append(row.MedicalSpeciality)
    return medical_specialities