from sqlalchemy import select
from sqlalchemy.orm import Session
from models.Address import Address
def list_addresses() -> list[Address]:
    addresses : list[Address] = []
    stmt = select(Address)
    for row in Session.execute(stmt):
        addresses.append(row.Address)
    return addresses