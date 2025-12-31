from flask import Blueprint, jsonify, request
import sys
from admin_bp.users.services.create_user import create_user
from admin_bp.doctors.services.create_doctor import create_doctor
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role
from admin_bp.exceptions.already_exists.DoctorAlreadyExistsException import DoctorAlreadyExistsException
from models.Doctor import Doctor
from admin_bp.patients.services import get_patient_by_name

# Creamos una instancia de Blueprint
# 'doctors_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
doctors_bp = Blueprint('doctors_bp', __name__)

# Definimos las rutas usando el Blueprint
@doctors_bp.route('/admin/doctors', methods=['POST'])
@needs_auth
@require_role(required_roles=["admin"])
def add_doctor(*args, **kwargs):
    datos = request.get_json()
    try:
        existing_doctor:Doctor = get_patient_by_name(datos['name'])
        if existing_doctor != None:
            raise DoctorAlreadyExistsException()
        created_user = create_user({
            'username':datos['username'],
            'password':datos['password']
        },user_role_str="doctor")
        created_doctor = create_doctor(created_user)
        return jsonify({'id': created_doctor.id_doctor, 'name': created_doctor.name})
    except DoctorAlreadyExistsException as e_patient_already_exists:
        print(e_patient_already_exists.__str__(),file=sys.stderr)
        print(e_patient_already_exists.__repr__(),file=sys.stderr)
        return jsonify({'message':'Paciente '+datos['name']+' ya existe.'}),409
    except (TypeError, ValueError) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

# ... (Añadir aquí las rutas POST, PUT, DELETE para médicos)