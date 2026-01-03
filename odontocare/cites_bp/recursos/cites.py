from flask import Blueprint, jsonify, request
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role

# Creamos una instancia de Blueprint
# 'cites_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
cites_bp = Blueprint('cites_bp', __name__)

# Definimos las rutas usando el Blueprint
@cites_bp.route('/cites', methods=['POST'])
@needs_auth
@require_role(required_roles=["admin","pacient"])
def add_appointment(*args, **kwargs):
    pass

@cites_bp.route('/cites', methods=['GET'])
@needs_auth
@require_role(required_roles=["admin","secretary","doctor"])
def list_appointment(*args, **kwargs):
    pass

@cites_bp.route('/cites/<int:id>', methods=['PUT'])
def cancel_appointment(id,*args, **kwargs):
    pass

# ... (Añadir aquí las rutas POST, PUT, DELETE para citas)