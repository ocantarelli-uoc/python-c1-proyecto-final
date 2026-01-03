from flask import Blueprint, jsonify, request
import sys
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role
from dtos.User import User
from services.add_appointment import add_appointment as orm_add_appointment
from exceptions.not_found.DoctorNotFoundException import DoctorNotFoundException
from exceptions.not_found.PatientNotFoundException import PatientNotFoundException
from exceptions.not_found.MedicalCenterNotFoundException import MedicalCenterNotFoundException
from exceptions.not_found.MedicalAppointmentStatusNotFoundException import MedicalAppointmentStatusNotFoundException
from exceptions.already_exists.MedicalAppointmentAlreadyExistsException import MedicalAppointmentAlreadyExistsException

# Creamos una instancia de Blueprint
# 'cites_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
cites_bp = Blueprint('cites_bp', __name__)

# Definimos las rutas usando el Blueprint
@cites_bp.route('/cites', methods=['POST'])
@needs_auth
@require_role(required_roles=["admin","pacient"])
def add_appointment(*args, **kwargs):
    datos = request.json()
    try:
        authorized_user : User = kwargs.get('authorized_user')
        appointment_input_dict = {
            'appointment_date':datos['appointment_date'],
            'id_doctor':datos['id_doctor'],
            'id_patient':datos['id_patient'],
            'id_medical_center':datos['id_medical_center'],
            'motiu':datos['motiu'],
            'id_action_user':authorized_user.id_user,
            'status':datos['status'],
        }
        created_appoinment = orm_add_appointment(appointment_input_dict)
    except (PatientNotFoundException) as e_user_not_found:
        print(e_user_not_found.__str__(),file=sys.stderr)
        print(e_user_not_found.__repr__(),file=sys.stderr)
        return jsonify({'message':'Paciente no encontrado!'}),404
    except DoctorNotFoundException as e_doctor_not_found:
        print(e_doctor_not_found.__str__(),file=sys.stderr)
        print(e_doctor_not_found.__repr__(),file=sys.stderr)
        return jsonify({'message':'Doctor no encontrado.'}),404
    except (MedicalCenterNotFoundException) as e_medical_center_not_found:
        print(e_medical_center_not_found.__str__(),file=sys.stderr)
        print(e_medical_center_not_found.__repr__(),file=sys.stderr)
        return jsonify({'message':'Centro Médico no encontrado!'}),404
    except (MedicalAppointmentStatusNotFoundException) as e_medical_appointment_not_found:
        print(e_medical_appointment_not_found.__str__(),file=sys.stderr)
        print(e_medical_appointment_not_found.__repr__(),file=sys.stderr)
        return jsonify({'message':'Cita Médica no encontrada!'}),404
    except (MedicalAppointmentAlreadyExistsException) as e_medical_appointment_already_exists:
        print(e_medical_appointment_already_exists.__str__(),file=sys.stderr)
        print(e_medical_appointment_already_exists.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ya hay cita médica para este doctor y hora!'}),409
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

@cites_bp.route('/cites', methods=['GET'])
@needs_auth
@require_role(required_roles=["admin","secretary","doctor"])
def list_appointment(*args, **kwargs):
    pass

@cites_bp.route('/cites/<int:id>', methods=['PUT'])
def cancel_appointment(id,*args, **kwargs):
    pass

# ... (Añadir aquí las rutas POST, PUT, DELETE para citas)