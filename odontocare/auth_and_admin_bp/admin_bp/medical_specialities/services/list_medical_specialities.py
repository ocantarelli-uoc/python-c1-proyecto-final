from sqlalchemy import select
from sqlalchemy.orm import Session
from models.MedicalSpeciality import MedicalSpeciality
def list_medical_specialities() -> list[MedicalSpeciality]:
    medical_specialities : list[MedicalSpeciality] = []
    stmt = select(MedicalSpeciality)
    for row in Session.execute(stmt):
        medical_specialities.append(row.MedicalSpeciality)
    return medical_specialities