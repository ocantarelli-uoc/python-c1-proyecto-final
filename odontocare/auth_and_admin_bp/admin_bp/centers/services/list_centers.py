from sqlalchemy import select
from sqlalchemy.orm import Session
from models.MedicalCenter import MedicalCenter
def list_centers() -> list[MedicalCenter]:
    centers : list[MedicalCenter] = []
    stmt = select(MedicalCenter)
    for row in Session.execute(stmt):
        centers.append(row.MedicalCenter)
    return centers