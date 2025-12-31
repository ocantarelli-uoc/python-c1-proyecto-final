from flask import request
from models.MedicalCenter import MedicalCenter
from models.Address import Address
from extensions import db

def create_center():
    try:
        datos = request.get_json()
        address:Address = Address.query.filter_by(name=datos["address_name"]).first()
        medical_center = MedicalCenter(name=datos["name"],
                                    address=address)
        db.session.add(medical_center)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    return medical_center