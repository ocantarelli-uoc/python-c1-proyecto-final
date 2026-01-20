from flask import Blueprint, jsonify, request
import sys
from admin_bp.centers.services.create_center import create_center
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role
from admin_bp.exceptions.already_exists.MedicalCenterAlreadyExistsException import MedicalCenterAlreadyExistsException
from admin_bp.exceptions.not_found.MedicalCenterNotFoundException import MedicalCenterNotFoundException
from models.MedicalCenter import MedicalCenter
from admin_bp.centers.services.get_center_by_name import get_center_by_name
from admin_bp.centers.services.list_centers import list_centers as orm_list_centers
from admin_bp.centers.services.get_center_by_id import get_medical_center_by_id as orm_get_medical_center_by_id
# Creamos una instancia de Blueprint
# "centers_bp" es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
centers_bp = Blueprint("centers_bp", __name__)

# Definimos las rutas usando el Blueprint
#It defines the endpoint for adding a center
@centers_bp.route("/admin/centres", methods=["POST"])
@needs_auth
@require_role(required_roles=["admin"])
def add_center(*args, **kwargs):
    datos = request.get_json()
    try:
        #It tries to get center by name
        existing_center:MedicalCenter = get_center_by_name(datos["name"])
        #It controls if the center already exists
        if existing_center is not None:
            raise MedicalCenterAlreadyExistsException()
        #It creates the center
        created_center = create_center()
        #It controls if the created center is not none
        if created_center is None:
            raise MedicalCenterNotFoundException()
        #It returns the created center in json format
        return jsonify({"id_medical_center": created_center.id_medical_center, "name": created_center.name, 
                        "address":{
                            "id_address":created_center.address.id_address,
                            "street":created_center.address.street,
                            "city":created_center.address.city,
                        }}),201
    #It captures if the medical center already exists
    except MedicalCenterAlreadyExistsException as e_center_already_exists:
        print(e_center_already_exists.__str__(),file=sys.stderr)
        print(e_center_already_exists.__repr__(),file=sys.stderr)
        return jsonify({"message":"Centro "+datos["name"]+" ya existe."}),409
    #It captures if the created medical center hasn't been found
    except MedicalCenterNotFoundException as e_center_not_exists:
        print(e_center_not_exists.__str__(),file=sys.stderr)
        print(e_center_not_exists.__repr__(),file=sys.stderr)
        return jsonify({"message":"Centro "+datos["name"]+" no se puede recuperar el centro recién creado."}),404
    #It captures if some error has ocurred   
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500

@centers_bp.route("/admin/centres", methods=["GET"])
@needs_auth
@require_role(required_roles=["admin"])
#It defines the endpoint for listing the previously created medical centers
def list_medical_centers(*args, **kwargs):
    try:
        #It gets the medical centers from repository from database
        medical_centers:list[MedicalCenter] = orm_list_centers()
        #It returns the medical centers as list in dictionary format for returning as json
        medical_centers_list = [{"id_medical_center": m_c.id_medical_center, "name": m_c.name,"address":{
            "id_address":m_c.address.id_address,
            "street":m_c.address.street,
            "city":m_c.address.city
        }} for m_c in medical_centers]
        #It returns the medical centers list as json format
        return jsonify(medical_centers_list)
    #It captures if some error has ocurred
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500

@centers_bp.route("/admin/centres/<int:id>", methods=["GET"])
@needs_auth
@require_role(required_roles=["admin"])
#It defines the endpoint for getting medical center by id
def get_medical_centers_by_id(id,*args, **kwargs):
    try:
        #It gets the medical center by id from repository from database
        medical_center : MedicalCenter = orm_get_medical_center_by_id(id)
        #It controls if the medical center hasn't been found
        if medical_center is None:
            raise MedicalCenterNotFoundException()
        #It returns the medical center in dictionary format for returning as json
        medical_center_dict = [{"id_medical_center": medical_center.id_medical_center, "name": medical_center.name,
            "address":{
                "id_address":medical_center.address.id_address,
                "street":medical_center.address.street,
                "city":medical_center.address.city
             }}]
        #It returns the medical center list as json format
        return jsonify(medical_center_dict)
    #It captures if the medical center hasn't been found
    except (MedicalCenterNotFoundException) as e_medical_center_not_found:
        print(e_medical_center_not_found.__str__(),file=sys.stderr)
        print(e_medical_center_not_found.__repr__(),file=sys.stderr)
        return jsonify({"message":"Centro Médico no encontrado!"}),404
    #It captures if some error has ocurred
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500