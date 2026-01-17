from flask import request
from models.MedicalCenter import MedicalCenter
from models.Address import Address
from extensions import db
#It defines the method for creating a medical center
def create_center():
    try:
        #It get the request body in json format
        datos = request.get_json()
        #It gets the address by id 
        address:Address = Address.query.filter_by(id_address=datos["id_address"]).first()
        #It gets the parameters from the body and it instances a medical center from MedicalCenter class
        #to storing it to database through ORM
        medical_center = MedicalCenter(name=datos["name"],
                                    address=address)
        #It adds the medical center to database through ORM
        db.session.add(medical_center)
        #It commits the changes
        db.session.commit()
    #It captures the generic exception
    except Exception as e:
        #It rollback the changes
        db.session.rollback()
        #It raise the generic exception
        raise e
    #It returns the medical center
    return medical_center