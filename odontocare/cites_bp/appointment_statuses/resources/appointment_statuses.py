from flask import Blueprint, jsonify, request
import sys
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role
from models.MedicalAppointmentStatus import MedicalAppointmentStatus
from appointment_statuses.services.create_medical_appointment_status import create_medical_appointment_status as orm_create_medical_appointment_status
from appointment_statuses.services.get_medical_appointment_status_by_id import get_medical_appointment_status_by_id as orm_get_medical_appointment_status_by_id
from appointment_statuses.services.list_medical_appointment_statuses import list_medical_appointment_statuses as orm_list_medical_appointment_statuses
from exceptions.already_exists.MedicalAppointmentStatusAlreadyExistsException import MedicalAppointmentStatusAlreadyExistsException
from exceptions.not_found.MedicalAppointmentStatusNotFoundException import MedicalAppointmentStatusNotFoundException
# Creamos una instancia de Blueprint
# "cites_bp" es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
appointment_statuses_bp = Blueprint("appointment_statuses_bp", __name__)

# Definimos las rutas usando el Blueprint
@appointment_statuses_bp.route("/estats_cites", methods=["POST"])
@needs_auth
@require_role(required_roles=["admin","pacient"])
#It defines the endpoint for adding an appointment status
def add_appointment_status(*args, **kwargs):
    datos = request.get_json()
    try:
        #It tries to create the appointment status
        appointment_status_input_dict = {
            "status_name":datos["status_name"],
        }
        created_appoinment_status : MedicalAppointmentStatus = orm_create_medical_appointment_status(appointment_status_input_dict)
        #It returns the created appointment status in json format
        return jsonify({"id_medical_status":created_appoinment_status.id_medical_status,
                        "name":created_appoinment_status.name}),201
    #It captures if the medical appointment status already exists
    except (MedicalAppointmentStatusAlreadyExistsException) as e_medical_appointment_status_already_exists:
        print(e_medical_appointment_status_already_exists.__str__(),file=sys.stderr)
        print(e_medical_appointment_status_already_exists.__repr__(),file=sys.stderr)
        return jsonify({"message":"Estado de Cita Médica ya existía!"}),409
    #It captures if an error has ocurred
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500

@appointment_statuses_bp.route("/estats_cites", methods=["GET"])
@needs_auth
@require_role(required_roles=["admin"])
#It defines the endpoint for listing appointment statuses
def list_medical_appointment_statuses(*args, **kwargs):
    try:
        #It gets the medical appointment statuses from repository from database
        medical_appointment_statuses = orm_list_medical_appointment_statuses()
        #It returns the medical appointment statuses as list in dictionary format for returning as json
        medical_appointment_statuses_list = [{"id": m_a_s.id_medical_status, "name": m_a_s.name} for m_a_s in medical_appointment_statuses]
        return jsonify(medical_appointment_statuses_list)
    #It controls if an error has ocurred
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500

@appointment_statuses_bp.route("/estats_cites/<int:id>", methods=["GET"])
@needs_auth
@require_role(required_roles=["admin"])
#It defines the endpoint for getting medical appointment status by id
def get_appointment_status_by_id(id,*args, **kwargs):
    try:
        #It gets the medical appointment status by id from repository from database
        appointment_status : MedicalAppointmentStatus = orm_get_medical_appointment_status_by_id(id)
        #It controls if the medical appointment status hasn't been found
        if appointment_status is None:
            raise MedicalAppointmentStatusNotFoundException()
        #It returns the medical appointment status in dictionary format for returning as json
        return jsonify({"id_medical_status":appointment_status.id_medical_status,
                        "name":appointment_status.name}),200
    #It captures if the medical appointment status hasn't been found
    except (MedicalAppointmentStatusNotFoundException) as e_medical_appointment_status_not_found:
        print(e_medical_appointment_status_not_found.__str__(),file=sys.stderr)
        print(e_medical_appointment_status_not_found.__repr__(),file=sys.stderr)
        return jsonify({"message":"Estado de Cita Médica no encontrado!"}),404
    #It captures if an error has ocurred
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500