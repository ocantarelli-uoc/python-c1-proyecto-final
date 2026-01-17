from flask import Blueprint, jsonify, request
import sys
from admin_bp.users.services.create_user import create_user
from admin_bp.patients.services.create_patient import create_patient
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role
from admin_bp.exceptions.already_exists.PatientAlreadyExistsException import PatientAlreadyExistsException
from models.Patient import Patient
from admin_bp.patients.services.get_patient_by_name import get_patient_by_name
from admin_bp.exceptions.not_found.PatientNotFoundException import PatientNotFoundException
from admin_bp.patients.services.list_patients import list_patients as orm_list_patients
from admin_bp.patients.services.get_patient_by_id import get_patient_by_id as orm_get_patient_by_id
from admin_bp.user_roles.enums.UserRoleEnum import UserRoleEnum
# Creamos una instancia de Blueprint
# "patients_bp" es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
patients_bp = Blueprint("patients_bp", __name__)

# Definimos las rutas usando el Blueprint
@patients_bp.route("/admin/pacients", methods=["POST"])
@needs_auth
@require_role(required_roles=["admin"])
#It defines the endpoint for adding a patient
def add_patient(*args, **kwargs):
    datos = request.get_json()
    try:
        #It tries to get patient by name
        existing_patient:Patient = get_patient_by_name(datos["name"])
        #It controls if the patient already exists
        if existing_patient is not None:
            raise PatientAlreadyExistsException()
        #It creates the user for patient
        created_user = create_user({
            "username":datos["username"],
            "password":datos["password"]
        },user_role_str=UserRoleEnum.PATIENT.value)
        #It creates the patient
        created_patient = create_patient(created_user)
        #It controls if the patient has been created
        if created_patient is None:
            raise PatientNotFoundException()
        #It returns the created patient in json format
        return jsonify({"id_patient": created_patient.id_patient, "name": created_patient.name,
                        "telephone":created_patient.telephone,
                        "is_active":created_patient.is_active,
                        "user":{"id_user": created_patient.user.id_user, "username": created_patient.user.username,
                        "user_role":{
                            "id_user_role":created_patient.user.user_role.id_user_role,
                            "name":created_patient.user.user_role.name,
                        }}})
    #It captures if the patient already exists
    except PatientAlreadyExistsException as e_patient_already_exists:
        print(e_patient_already_exists.__str__(),file=sys.stderr)
        print(e_patient_already_exists.__repr__(),file=sys.stderr)
        return jsonify({"message":"Paciente "+datos["name"]+" ya existe."}),409
    #It captures if created patient hasn't been found
    except PatientNotFoundException as e_patient_not_found:
        print(e_patient_not_found.__str__(),file=sys.stderr)
        print(e_patient_not_found.__repr__(),file=sys.stderr)
        return jsonify({"message":"Paciente "+datos["name"]+" no se encuentra."}),404
    #It captures if an error has ocurred
    except (TypeError, ValueError,Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500

@patients_bp.route("/admin/pacients", methods=["GET"])
@needs_auth
@require_role(required_roles=["admin"])
#It defines the endpoint for listing the previously created patients
def list_patients(*args, **kwargs):
    try:
        #It gets the patients from repository from database
        patients:list[Patient] = orm_list_patients()
        #It returns the patients as list in dictionary format for returning as json
        patients_list = [{"id": p.id_patient, "name": p.name} for p in patients]
        return jsonify(patients_list)
    #It controls if an error has ocurred
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500
    
@patients_bp.route("/admin/pacients/<int:id>", methods=["GET"])
@needs_auth
@require_role(required_roles=["admin"])
#It defines the endpoint for getting patient by id
def get_patient_by_id(id,*args, **kwargs):
    try:
        #It gets the patient by id from repository from database
        patient : Patient = orm_get_patient_by_id(id)
        #It controls if the patient hasn't been found
        if patient is None:
            raise PatientNotFoundException()
        #It returns the patient in dictionary format for returning as json
        patient_dict = [{"id_patient": patient.id_patient, "name": patient.name
                        ,
                        "user":{
                            "id_user":patient.user.id_user,
                            "username":patient.user.username,
                            "user_role":{
                                "id_user_role":patient.user.user_role.id_user_role,
                                "name":patient.user.user_role.name,
                            }
                        }
                        ,"telephone":patient.telephone,
                        "is_active":patient.is_active}]
        return jsonify(patient_dict)
    #It captures if the patient hasn't been found
    except (PatientNotFoundException) as e_user_not_found:
        print(e_user_not_found.__str__(),file=sys.stderr)
        print(e_user_not_found.__repr__(),file=sys.stderr)
        return jsonify({"message":"Paciente no encontrado!"}),404
    #It captures if an error has ocurred
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500