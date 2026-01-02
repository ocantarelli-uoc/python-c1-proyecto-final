from flask import Blueprint, jsonify, request
import sys
from admin_bp.medical_specialities.services.create_medical_speciality import create_medical_speciality
from admin_bp.medical_specialities.services.get_medical_speciality_by_id import get_medical_speciality_by_id
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role
from admin_bp.exceptions.already_exists.MedicalSpecialityAlreadyExistsException import MedicalSpecialityAlreadyExistsException
from models.MedicalSpeciality import MedicalSpeciality
from admin_bp.medical_specialities.services.get_medical_speciality_by_name import get_medical_speciality_by_name
from admin_bp.medical_specialities.services.list_medical_specialities import list_medical_specialities as orm_list_medical_specialities
from admin_bp.exceptions.not_found.MedicalSpecialityNotFoundException import MedicalSpecialityNotFoundException
# Creamos una instancia de Blueprint
# 'medical_specialities_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
medical_specialities_bp = Blueprint('medical_specialities_bp', __name__)

# Definimos las rutas usando el Blueprint
@medical_specialities_bp.route('/admin/especialitats_mediques', methods=['POST'])
@needs_auth
@require_role(required_roles=["admin"])
def add_medical_speciality(*args, **kwargs):
    datos = request.get_json()
    try:
        existing_medical_speciality:MedicalSpeciality = get_medical_speciality_by_name(datos["medical_speciality_name"])
        if existing_medical_speciality != None:
            raise MedicalSpecialityAlreadyExistsException()
        created_medical_speciality = create_medical_speciality()
        medical_speciality = get_medical_speciality_by_id(created_medical_speciality.id_medical_speciality)
        if medical_speciality == None:
            raise MedicalSpecialityNotFoundException()
        return jsonify({'id': medical_speciality.id_medical_speciality, 'name': created_medical_speciality.name})
    except MedicalSpecialityAlreadyExistsException as e_medical_speciality_already_exists:
        print(e_medical_speciality_already_exists.__str__(),file=sys.stderr)
        print(e_medical_speciality_already_exists.__repr__(),file=sys.stderr)
        return jsonify({'message':'Especialidad Médica '+datos["medical_speciality_name"]+' ya existe.'}),409
    except MedicalSpecialityNotFoundException as e_medical_speciality_not_found:
        print(e_medical_speciality_not_found.__str__(),file=sys.stderr)
        print(e_medical_speciality_not_found.__repr__(),file=sys.stderr)
        return jsonify({'message':'Especialidad Médica '+datos["medical_speciality_name"]+' no se encuentra recién creado.'}),404
    except (TypeError, ValueError,Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

@medical_specialities_bp.route('/admin/especialitats_mediques', methods=['GET'])
@needs_auth
@require_role(required_roles=["admin"])
def list_medical_specialities(*args, **kwargs):
    try:
        medical_specialities:list[MedicalSpeciality] = orm_list_medical_specialities()
        medical_specialities_list = [{'id': m_s.id_medical_speciality, 'name': m_s.name} for m_s in medical_specialities]
        return jsonify(medical_specialities_list)
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

# ... (Añadir aquí las rutas POST, PUT, DELETE para usuarios)