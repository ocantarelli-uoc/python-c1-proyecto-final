from models.Address import Address
from flask import Blueprint, jsonify, request
import sys
from admin_bp.addresses.services.create_address import create_address
from admin_bp.exceptions.already_exists.AddressAlreadyExistsException import AddressAlreadyExistsException
from admin_bp.exceptions.not_found.AddressNotFoundException import AddressNotFoundException
from admin_bp.addresses.services.get_address_by_filter import get_address_by_filter

# Creamos una instancia de Blueprint
# 'address_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
address_bp = Blueprint('address_bp', __name__)

# Definimos las rutas usando el Blueprint
@address_bp.route('/admin/adreces', methods=['POST'])
def add_address():
    datos = request.get_json()
    try:
        existing_address:Address = get_address_by_filter(datos['street'],datos['city'])
        if existing_address != None:
            raise AddressAlreadyExistsException()
        created_address = create_address()
        if create_address == None:
            raise AddressNotFoundException()
        return jsonify({'id': created_address.id_address, 'street': created_address.street, 
                        'city':created_address.city})
    except AddressAlreadyExistsException as e_address_already_exists:
        print(e_address_already_exists.__str__(),file=sys.stderr)
        print(e_address_already_exists.__repr__(),file=sys.stderr)
        return jsonify({'message':'Dirección calle:'+datos['street']+',city:'+datos['city']+' ya existe.'}),409
    except AddressNotFoundException as e_address_not_found:
        print(e_address_not_found.__str__(),file=sys.stderr)
        print(e_address_not_found.__repr__(),file=sys.stderr)
        return jsonify({'message':'Dirección calle:'+datos['street']+',city:'+datos['city']+' ha habido algún problema al crearse, y no se encuentra objeto creado.'}),404
    except (TypeError, ValueError) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

# ... (Añadir aquí las rutas POST, PUT, DELETE para direcciones)