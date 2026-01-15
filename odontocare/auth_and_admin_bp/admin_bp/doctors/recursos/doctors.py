from flask import Blueprint, jsonify, request
import sys
from admin_bp.users.services.create_user import create_user
from admin_bp.doctors.services.create_doctor import create_doctor
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role
from admin_bp.exceptions.already_exists.DoctorAlreadyExistsException import DoctorAlreadyExistsException
from admin_bp.exceptions.not_found.DoctorNotFoundException import DoctorNotFoundException
from models.Doctor import Doctor
from admin_bp.doctors.services.get_doctor_by_name import get_doctor_by_name
from admin_bp.doctors.services.list_doctors import list_doctors as orm_list_doctors
from admin_bp.doctors.services.get_doctor_by_id import get_doctor_by_id as orm_get_doctor_by_id
from admin_bp.user_roles.enums.UserRoleEnum import UserRoleEnum
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
        existing_doctor:Doctor = get_doctor_by_name(datos['name'])
        if existing_doctor != None:
            raise DoctorAlreadyExistsException()
        created_user = create_user({
            'username':datos['username'],
            'password':datos['password']
        },user_role_str=UserRoleEnum.DOCTOR.value)
        created_doctor = create_doctor(created_user)
        if created_doctor is None:
            raise DoctorNotFoundException()
        return jsonify({'id_doctor': created_doctor.id_doctor, 'name': created_doctor.name,'user':{'id_user': created_doctor.user.id_user, 'username': created_doctor.user.username,
                        'user_role':{
                            'id_user_role':created_doctor.user.user_role.id_user_role,
                            'name':created_doctor.user.user_role.name,
                        }},
                        'medical_speciality':{
                            'id_medical_speciality':created_doctor.medical_speciality.id_medical_speciality,
                            'name':created_doctor.medical_speciality.name,
                        }})
    except DoctorAlreadyExistsException as e_doctor_already_exists:
        print(e_doctor_already_exists.__str__(),file=sys.stderr)
        print(e_doctor_already_exists.__repr__(),file=sys.stderr)
        return jsonify({'message':'Doctor '+datos['name']+' ya existe.'}),409
    except DoctorNotFoundException as e_doctor_not_found:
        print(e_doctor_not_found.__str__(),file=sys.stderr)
        print(e_doctor_not_found.__repr__(),file=sys.stderr)
        return jsonify({'message':'Doctor '+datos['name']+' no se encuentra recién creado.'}),404
    except (TypeError, ValueError,Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

@doctors_bp.route('/admin/doctors', methods=['GET'])
@needs_auth
@require_role(required_roles=["admin"])
def list_doctors(*args, **kwargs):
    try:
        doctors:list[Doctor] = orm_list_doctors()
        doctors_list = [{'id': d.id_doctor, 'name': d.name} for d in doctors]
        return jsonify(doctors_list)
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

@doctors_bp.route('/admin/doctors/<int:id>', methods=['GET'])
@needs_auth
@require_role(required_roles=["admin"])
def get_doctor_by_id(id,*args, **kwargs):
    try:
        doctor : Doctor = orm_get_doctor_by_id(id)
        if doctor is None:
            raise DoctorNotFoundException()
        doctor_dict = [{'id_doctor': doctor.id_doctor, 'name': doctor.name
                        ,'medical_speciality':{
                            'id_medical_speciality':doctor.medical_speciality.id_medical_speciality,
                            'name':doctor.medical_speciality.name,
                        },
                        'user':{
                            'id_user':doctor.user.id_user,
                            'username':doctor.user.username,
                            'user_role':{
                                'id_user_role':doctor.user.user_role.id_user_role,
                                'name':doctor.user.user_role.name,
                            }
                        }}]
        return jsonify(doctor_dict)
    except (DoctorNotFoundException) as e_doctor_not_found:
        print(e_doctor_not_found.__str__(),file=sys.stderr)
        print(e_doctor_not_found.__repr__(),file=sys.stderr)
        return jsonify({'message':'Doctor no encontrado!'}),404
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

# ... (Añadir aquí las rutas POST, PUT, DELETE para médicos)