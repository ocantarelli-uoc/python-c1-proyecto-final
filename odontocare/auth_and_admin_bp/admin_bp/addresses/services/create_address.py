from flask import request
from models.Address import Address
from extensions import db

def create_address():
    try:
        datos = request.get_json()
        address = Address(street=datos["street"],city=datos["city"])
        db.session.add(address)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    return address