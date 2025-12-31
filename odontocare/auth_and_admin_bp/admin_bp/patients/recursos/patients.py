from flask import Blueprint, jsonify, request
import sys
from admin_bp.users.services.create_user import create_user
from admin_bp.patients.services.create_patient import create_patient
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role
from admin_bp.exceptions.already_exists.PatientAlreadyExistsException import PatientAlreadyExistsException
from models.Patient import Patient
from admin_bp.patients.services.get_patient_by_name import get_patient_by_name

# Creamos una instancia de Blueprint
# 'patients_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
patients_bp = Blueprint('patients_bp', __name__)

# Definimos las rutas usando el Blueprint
@patients_bp.route('/admin/pacients', methods=['POST'])
@needs_auth
@require_role(required_roles=["admin"])
def add_patient(*args, **kwargs):
    datos = request.get_json()
    try:
        existing_patient:Patient = get_patient_by_name(datos['role_name'])
        if existing_patient != None:
            raise PatientAlreadyExistsException()
        created_user = create_user({
            'username':datos['username'],
            'password':datos['password']
        },user_role_str="patient")
        created_patient = create_patient(created_user)
        return jsonify({'id': created_patient.id_patient, 'name': created_patient.name})
    except PatientAlreadyExistsException as e_patient_already_exists:
        print(e_patient_already_exists.__str__(),file=sys.stderr)
        print(e_patient_already_exists.__repr__(),file=sys.stderr)
        return jsonify({'message':'Paciente '+datos['name']+' ya existe.'}),409
    except (TypeError, ValueError) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

# ... (Añadir aquí las rutas POST, PUT, DELETE para pacientes)