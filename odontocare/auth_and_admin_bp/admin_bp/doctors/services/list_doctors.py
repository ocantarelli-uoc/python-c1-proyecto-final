from sqlalchemy import select
from sqlalchemy.orm import Session
from models.Doctor import Doctor
def list_doctors() -> list[Doctor]:
    doctors : list[Doctor] = []
    stmt = select(Doctor)
    for row in Session.execute(stmt):
        doctors.append(row.Doctor)
    return doctors