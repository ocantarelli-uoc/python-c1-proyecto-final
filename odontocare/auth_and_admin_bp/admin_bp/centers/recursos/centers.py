from flask import Blueprint, jsonify, request
import sys
from admin_bp.centers.services.create_center import create_center
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role

# Creamos una instancia de Blueprint
# 'centers_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
centers_bp = Blueprint('centers_bp', __name__)

# Definimos las rutas usando el Blueprint
@centers_bp.route('/admin/centres', methods=['POST'])
@needs_auth
@require_role(required_roles=["admin"])
def add_center(*args, **kwargs):
    try:
        created_center = create_center()
        return jsonify({'id': created_center.id_medical_center, 'name': created_center.name})
    except Exception as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

# ... (Añadir aquí las rutas POST, PUT, DELETE para centros)