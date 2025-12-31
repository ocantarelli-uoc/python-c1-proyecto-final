from flask import Blueprint, jsonify, request
import sys
from admin_bp.centers.services.create_center import create_center
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role
from admin_bp.exceptions.already_exists.MedicalCenterAlreadyExistsException import MedicalCenterAlreadyExistsException
from admin_bp.exceptions.not_found.MedicalCenterNotFoundException import MedicalCenterNotFoundException
from models.MedicalCenter import MedicalCenter
from admin_bp.centers.services.get_center_by_name import get_center_by_name

# Creamos una instancia de Blueprint
# 'centers_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
centers_bp = Blueprint('centers_bp', __name__)

# Definimos las rutas usando el Blueprint
@centers_bp.route('/admin/centres', methods=['POST'])
@needs_auth
@require_role(required_roles=["admin"])
def add_center(*args, **kwargs):
    datos = request.get_json()
    try:
        existing_center:MedicalCenter = get_center_by_name(datos['name'])
        if existing_center != None:
            raise MedicalCenterAlreadyExistsException()
        created_center = create_center()
        if created_center == None:
            raise MedicalCenterNotFoundException()
        return jsonify({'id': created_center.id_medical_center, 'name': created_center.name})
    except MedicalCenterAlreadyExistsException as e_center_already_exists:
        print(e_center_already_exists.__str__(),file=sys.stderr)
        print(e_center_already_exists.__repr__(),file=sys.stderr)
        return jsonify({'message':'Centro '+datos['name']+' ya existe.'}),409
    except MedicalCenterNotFoundException as e_center_not_exists_exists:
        print(e_center_not_exists_exists.__str__(),file=sys.stderr)
        print(e_center_not_exists_exists.__repr__(),file=sys.stderr)
        return jsonify({'message':'Centro '+datos['name']+' no se puede recuperar el centro recién creado.'}),404
    except (TypeError, ValueError) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

# ... (Añadir aquí las rutas POST, PUT, DELETE para centros)