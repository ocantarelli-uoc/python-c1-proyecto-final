from flask import request
from models.Address import Address
from extensions import db
#It defines the method for creating an addresss
def create_address():
    try:
        #It get the request body in json format
        datos = request.get_json()
        #It gets the parameters from the body and it instances an address from Address class
        #to storing it to database through ORM
        address = Address(street=datos["street"],city=datos["city"])
        #It adds the address to database through ORM
        db.session.add(address)
        #It commit the changes
        db.session.commit()
    #It captures the generic exception
    except Exception as e:
        #It rollback the changes
        db.session.rollback()
        #It raise the generic exception above to the method which invoked this.
        raise e
    #It returns the created address
    return address