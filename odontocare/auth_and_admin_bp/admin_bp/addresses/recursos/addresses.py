from models.Address import Address
from flask import Blueprint, jsonify, request
import sys
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role
from admin_bp.addresses.services.create_address import create_address
from admin_bp.exceptions.already_exists.AddressAlreadyExistsException import AddressAlreadyExistsException
from admin_bp.exceptions.not_found.AddressNotFoundException import AddressNotFoundException
from admin_bp.addresses.services.get_address_by_filter import get_address_by_filter
from admin_bp.addresses.services.list_addresses import list_addresses as orm_list_address
from admin_bp.addresses.services.get_address_by_id import get_address_by_id as orm_get_address_by_id
# Creamos una instancia de Blueprint
# "address_bp" es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
address_bp = Blueprint("address_bp", __name__)

# Definimos las rutas usando el Blueprint
@address_bp.route("/admin/adreces", methods=["POST"])
@needs_auth
@require_role(required_roles=["admin"])
def add_address(*args, **kwargs):
    datos = request.get_json()
    try:
        existing_address:Address = get_address_by_filter(datos["street"],datos["city"])
        if existing_address != None:
            raise AddressAlreadyExistsException()
        created_address = create_address()
        if create_address is None:
            raise AddressNotFoundException()
        return jsonify({"id_address": created_address.id_address, "street": created_address.street, 
                        "city":created_address.city})
    except AddressAlreadyExistsException as e_address_already_exists:
        print(e_address_already_exists.__str__(),file=sys.stderr)
        print(e_address_already_exists.__repr__(),file=sys.stderr)
        return jsonify({"message":"Dirección calle:"+datos["street"]+",city:"+datos["city"]+" ya existe."}),409
    except AddressNotFoundException as e_address_not_found:
        print(e_address_not_found.__str__(),file=sys.stderr)
        print(e_address_not_found.__repr__(),file=sys.stderr)
        return jsonify({"message":"Dirección calle:"+datos["street"]+",city:"+datos["city"]+" ha habido algún problema al crearse, y no se encuentra objeto creado."}),404
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500
    
@address_bp.route("/admin/adreces", methods=["GET"])
@needs_auth
@require_role(required_roles=["admin"])
def list_addresses(*args, **kwargs):
    try:
        addresses:list[Address] = orm_list_address()
        addresses_list = [{"id_address":a.id_address,
            "street":a.street,
            "city":a.city} for a in addresses]
        return jsonify(addresses_list)
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500

@address_bp.route("/admin/adreces/<int:id>", methods=["GET"])
@needs_auth
@require_role(required_roles=["admin"])
def get_address_by_id(id,*args, **kwargs):
    try:
        address : Address = orm_get_address_by_id(id)
        if address is None:
            raise AddressNotFoundException()
        user_role_dict = [{"id_address":address.id_address,
                "street":address.street,
                "city":address.city}]
        return jsonify(user_role_dict)
    except (AddressNotFoundException) as e_address_not_found:
        print(e_address_not_found.__str__(),file=sys.stderr)
        print(e_address_not_found.__repr__(),file=sys.stderr)
        return jsonify({"message":"Dirección no encontrada!"}),404
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500

# ... (Añadir aquí las rutas POST, PUT, DELETE para direcciones)