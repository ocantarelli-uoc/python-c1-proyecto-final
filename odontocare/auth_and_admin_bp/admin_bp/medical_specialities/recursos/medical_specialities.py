from flask import Blueprint, jsonify, request
from admin_bp.medical_specialities.services.create_medical_speciality import create_medical_speciality
from admin_bp.medical_specialities.services.get_medical_speciality_by_id import get_medical_speciality_by_id
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role
# Creamos una instancia de Blueprint
# 'medical_specialities_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
medical_specialities_bp = Blueprint('medical_specialities_bp', __name__)

# Definimos las rutas usando el Blueprint
@medical_specialities_bp.route('/admin/especialitats_mediques', methods=['POST'])
@needs_auth
@require_role(required_roles=["admin"])
def add_medical_speciality(*args, **kwargs):
    try:
        created_medical_speciality = create_medical_speciality()
        medical_speciality = get_medical_speciality_by_id(created_medical_speciality.id_medical_speciality)
        return jsonify({'id': medical_speciality.id_medical_speciality, 'name': created_medical_speciality.name})
    except Exception as e:
        return jsonify({'message':'Ha ocurrido algún error!'}),500

# ... (Añadir aquí las rutas POST, PUT, DELETE para usuarios)