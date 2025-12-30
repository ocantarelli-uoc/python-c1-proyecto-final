from flask import Blueprint, jsonify, request
from admin_bp.addresses.services.create_address import create_address

# Creamos una instancia de Blueprint
# 'address_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
address_bp = Blueprint('address_bp', __name__)

# Definimos las rutas usando el Blueprint
@address_bp.route('/admin/adreces', methods=['POST'])
def add_address():
    created_address = create_address()
    return jsonify({'id': created_address.id_address, 'street': created_address.street, 
                    'city':created_address.city})

# ... (Añadir aquí las rutas POST, PUT, DELETE para direcciones)