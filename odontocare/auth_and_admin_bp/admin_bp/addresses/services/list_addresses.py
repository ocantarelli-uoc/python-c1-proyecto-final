from sqlalchemy import select
from extensions import db
from models.Address import Address
def list_addresses() -> list[Address]:
    addresses : list[Address] = []
    stmt = select(Address)
    for row in db.session.execute(stmt):
        addresses.append(row.Address)
    return addresses