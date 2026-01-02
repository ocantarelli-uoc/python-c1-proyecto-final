from sqlalchemy import select
from extensions import db
from models.Doctor import Doctor
def list_doctors() -> list[Doctor]:
    doctors : list[Doctor] = []
    stmt = select(Doctor)
    for row in db.session.execute(stmt):
        doctors.append(row.Doctor)
    return doctors