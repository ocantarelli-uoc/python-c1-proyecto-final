from flask import Blueprint, jsonify, request

# Creamos una instancia de Blueprint
# 'cites_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
cites_bp = Blueprint('cites_bp', __name__)

# Definimos las rutas usando el Blueprint
@cites_bp.route('/cites', methods=['POST'])
def add_appointment(*args, **kwargs):
    pass

@cites_bp.route('/cites', methods=['GET'])
def get_appointment(*args, **kwargs):
    pass

@cites_bp.route('/cites/<int:id>', methods=['PUT'])
def cancel_appointment(id,*args, **kwargs):
    pass

# ... (Añadir aquí las rutas POST, PUT, DELETE para citas)