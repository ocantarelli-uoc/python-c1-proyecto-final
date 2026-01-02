from sqlalchemy import select
from extensions import db
from models.MedicalCenter import MedicalCenter
def list_centers() -> list[MedicalCenter]:
    centers : list[MedicalCenter] = []
    stmt = select(MedicalCenter)
    for row in db.session.execute(stmt):
        centers.append(row.MedicalCenter)
    return centers