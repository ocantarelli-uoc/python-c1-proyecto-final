from flask import request
from models.Address import Address
from extensions import db

def create_address():
    datos = request.get_json()
    address = Address(street=datos["street"],city=datos["city"])
    db.session.add(address)
    db.session.commit()
    return address