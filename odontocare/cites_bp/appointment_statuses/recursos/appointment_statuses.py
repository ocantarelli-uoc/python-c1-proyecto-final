from flask import Blueprint, jsonify, request
import sys
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role
from models.MedicalAppointmentStatus import MedicalAppointmentStatus
from appointment_statuses.services.create_medical_appointment_status import create_medical_appointment_status as orm_create_medical_appointment_status
from appointment_statuses.services.get_medical_appointment_status_by_id import get_medical_appointment_status_by_id as orm_get_medical_appointment_status_by_id
from exceptions.already_exists.MedicalAppointmentStatusAlreadyExistsException import MedicalAppointmentStatusAlreadyExistsException
from exceptions.not_found.MedicalAppointmentStatusNotFoundException import MedicalAppointmentStatusNotFoundException
# Creamos una instancia de Blueprint
# 'cites_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
appointment_statuses_bp = Blueprint('appointment_statuses_bp', __name__)

# Definimos las rutas usando el Blueprint
@appointment_statuses_bp.route('/estats_cites', methods=['POST'])
@needs_auth
@require_role(required_roles=["admin","pacient"])
def add_appointment(*args, **kwargs):
    datos = request.get_json()
    try:
        appointment_status_input_dict = {
            'status_name':datos['status_name'],
        }
        created_appoinment_status : MedicalAppointmentStatus = orm_create_medical_appointment_status(appointment_status_input_dict)
        return jsonify({'id_medical_status':created_appoinment_status.id_medical_status,
                        'name':created_appoinment_status.name}),201
    except (MedicalAppointmentStatusAlreadyExistsException) as e_medical_appointment_status_already_exists:
        print(e_medical_appointment_status_already_exists.__str__(),file=sys.stderr)
        print(e_medical_appointment_status_already_exists.__repr__(),file=sys.stderr)
        return jsonify({'message':'Estado de Cita Médica ya existía!'}),404
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

@appointment_statuses_bp.route('/estats_cites', methods=['GET'])
@needs_auth
@require_role(required_roles=["admin"])
def list_appointment_statuses(*args, **kwargs):
    pass

@appointment_statuses_bp.route('/estats_cites/<int:id>', methods=['GET'])
@needs_auth
@require_role(required_roles=["admin"])
def get_appointment_status_by_id(id,*args, **kwargs):
    try:
        appointment_status : MedicalAppointmentStatus = orm_get_medical_appointment_status_by_id(id)
        return jsonify({'id_medical_status':appointment_status.id_medical_status,
                        'name':appointment_status.name}),200
    except (MedicalAppointmentStatusNotFoundException) as e_medical_appointment_status_not_found:
        print(e_medical_appointment_status_not_found.__str__(),file=sys.stderr)
        print(e_medical_appointment_status_not_found.__repr__(),file=sys.stderr)
        return jsonify({'message':'Estado de Cita Médica no existe!'}),404
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500


# ... (Añadir aquí las rutas POST, PUT, DELETE para citas)