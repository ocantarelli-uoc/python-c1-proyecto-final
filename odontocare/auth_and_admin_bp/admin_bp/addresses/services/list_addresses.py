from sqlalchemy import select
from extensions import db
from models.Address import Address
#It defines the method for listing addresses
def list_addresses() -> list[Address]:
    #It declares the variable for adding the addresses gotten
    #from database through ORM
    addresses : list[Address] = []
    #It selects the addresses from database through ORM
    stmt = select(Address)
    #for every address gotten from database
    for row in db.session.execute(stmt):
        #It adds the current address to the list
        addresses.append(row.Address)
    #It returns the address list gotten from database
    #through ORM
    return addresses