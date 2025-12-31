from flask import Blueprint, jsonify, request
import sys
from admin_bp.addresses.services.create_address import create_address

# Creamos una instancia de Blueprint
# 'address_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
address_bp = Blueprint('address_bp', __name__)

# Definimos las rutas usando el Blueprint
@address_bp.route('/admin/adreces', methods=['POST'])
def add_address():
    try:
        created_address = create_address()
        return jsonify({'id': created_address.id_address, 'street': created_address.street, 
                        'city':created_address.city})
    except Exception as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

# ... (Añadir aquí las rutas POST, PUT, DELETE para direcciones)