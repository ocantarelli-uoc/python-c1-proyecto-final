from flask import Blueprint, jsonify, request
import sys
from admin_bp.users.services.create_user import create_user
from admin_bp.doctors.services.create_doctor import create_doctor
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role
from admin_bp.exceptions.already_exists.DoctorAlreadyExistsException import DoctorAlreadyExistsException
from admin_bp.exceptions.not_found.DoctorNotFoundException import DoctorNotFoundException
from models.Doctor import Doctor
from models.User import User
from admin_bp.doctors.services.get_doctor_by_name import get_doctor_by_name
from admin_bp.doctors.services.list_doctors import list_doctors as orm_list_doctors
from admin_bp.doctors.services.get_doctor_by_id import get_doctor_by_id as orm_get_doctor_by_id
from admin_bp.user_roles.enums.UserRoleEnum import UserRoleEnum
from admin_bp.users.services.get_user_by_username import get_user_by_username
from admin_bp.exceptions.already_exists.UserAlreadyExistsException import UserAlreadyExistsException
# Creamos una instancia de Blueprint
# "doctors_bp" es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
doctors_bp = Blueprint("doctors_bp", __name__)

# Definimos las rutas usando el Blueprint
@doctors_bp.route("/admin/doctors", methods=["POST"])
@needs_auth
@require_role(required_roles=["admin"])
#It defines the endpoint for adding a doctor
def add_doctor(*args, **kwargs):
    datos = request.get_json()
    try:
        #It tries to get doctor by name
        existing_doctor:Doctor = get_doctor_by_name(datos["name"])
        #It controls if the doctor already exists
        if existing_doctor is not None:
            raise DoctorAlreadyExistsException()
        else:
            existing_doctor_user:User = get_user_by_username(datos["username"])
            #It controls if the doctor already exists
            if existing_doctor_user is not None:
                raise UserAlreadyExistsException()
        #It creates the user for doctor
        created_user = create_user({
            "username":datos["username"],
            "password":datos["password"]
        },user_role_str=UserRoleEnum.DOCTOR.value)
        #It creates the doctor
        created_doctor = create_doctor(created_user)
        #It controls if the created doctor is not none
        if created_doctor is None:
            raise DoctorNotFoundException()
        #It returns the created doctor in json format
        return jsonify({"id_doctor": created_doctor.id_doctor, "name": created_doctor.name,"user":{"id_user": created_doctor.user.id_user, "username": created_doctor.user.username,
                        "user_role":{
                            "id_user_role":created_doctor.user.user_role.id_user_role,
                            "name":created_doctor.user.user_role.name,
                        }},
                        "medical_speciality":{
                            "id_medical_speciality":created_doctor.medical_speciality.id_medical_speciality,
                            "name":created_doctor.medical_speciality.name,
                        }}),201
    #It captures if doctor already exists
    except DoctorAlreadyExistsException as e_doctor_already_exists:
        print(e_doctor_already_exists.__str__(),file=sys.stderr)
        print(e_doctor_already_exists.__repr__(),file=sys.stderr)
        return jsonify({"message":"Doctor "+datos["name"]+" ya existe."}),409
    except UserAlreadyExistsException as e_user_already_exists:
        print(e_user_already_exists.__str__(),file=sys.stderr)
        print(e_user_already_exists.__repr__(),file=sys.stderr)
        return jsonify({"message":"Usuario para el que se quiere crear Doctor "+datos["name"]+" ya existe."}),409
    #It captures if created doctor hasn't been found
    except DoctorNotFoundException as e_doctor_not_found:
        print(e_doctor_not_found.__str__(),file=sys.stderr)
        print(e_doctor_not_found.__repr__(),file=sys.stderr)
        return jsonify({"message":"Doctor "+datos["name"]+" no se encuentra recién creado."}),404
    #It captures if an error has ocurred
    except (TypeError, ValueError,Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500

@doctors_bp.route("/admin/doctors", methods=["GET"])
@needs_auth
@require_role(required_roles=["admin"])
#It defines the endpoint for listing the previously created doctors
def list_doctors(*args, **kwargs):
    try:
        #It gets the medical doctors from repository from database
        doctors:list[Doctor] = orm_list_doctors()
        #It returns the doctors as list in dictionary format for returning as json
        doctors_list = [{"id": d.id_doctor, "name": d.name} for d in doctors]
        return jsonify(doctors_list)
    #It controls if an error has ocurred
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500

@doctors_bp.route("/admin/doctors/<int:id>", methods=["GET"])
@needs_auth
@require_role(required_roles=["admin"])
#It defines the endpoint for getting doctor by id
def get_doctor_by_id(id,*args, **kwargs):
    try:
        #It gets the doctor by id from repository from database
        doctor : Doctor = orm_get_doctor_by_id(id)
        #It controls if the doctor hasn't been found
        if doctor is None:
            raise DoctorNotFoundException()
        #It returns the doctor in dictionary format for returning as json
        doctor_dict = [{"id_doctor": doctor.id_doctor, "name": doctor.name
                        ,"medical_speciality":{
                            "id_medical_speciality":doctor.medical_speciality.id_medical_speciality,
                            "name":doctor.medical_speciality.name,
                        },
                        "user":{
                            "id_user":doctor.user.id_user,
                            "username":doctor.user.username,
                            "user_role":{
                                "id_user_role":doctor.user.user_role.id_user_role,
                                "name":doctor.user.user_role.name,
                            }
                        }}]
        return jsonify(doctor_dict)
    #It captures if the doctor hasn't been found
    except (DoctorNotFoundException) as e_doctor_not_found:
        print(e_doctor_not_found.__str__(),file=sys.stderr)
        print(e_doctor_not_found.__repr__(),file=sys.stderr)
        return jsonify({"message":"Doctor no encontrado!"}),404
    #It captures if an error has ocurred
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500