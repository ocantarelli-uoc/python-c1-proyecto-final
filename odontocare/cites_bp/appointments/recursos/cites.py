from flask import Blueprint, jsonify, request
import sys
import datetime
from zoneinfo import ZoneInfo
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role
from dtos.User import User
from models.MedicalAppointment import MedicalAppointment
from enums.MedicalAppointmentStatusEnum import MedicalAppointmentStatusEnum
from appointments.services.add_appointment import add_appointment as orm_add_appointment
from appointments.services.modify_appointment_status import modify_appointment_status as orm_modify_appointment_status
from exceptions.not_found.DoctorNotFoundException import DoctorNotFoundException
from exceptions.not_found.PatientNotFoundException import PatientNotFoundException
from exceptions.not_found.MedicalCenterNotFoundException import MedicalCenterNotFoundException
from exceptions.not_found.MedicalAppointmentStatusNotFoundException import MedicalAppointmentStatusNotFoundException
from exceptions.already_exists.MedicalAppointmentAlreadyExistsException import MedicalAppointmentAlreadyExistsException
from exceptions.not_found.MedicalAppointmentNotFoundException import MedicalAppointmentNotFoundException
from exceptions.action_already_applied.MedicalAppointmentAlreadyCancelledException import MedicalAppointmentAlreadyCancelledException
from exceptions.action_already_applied.MedicalAppointmentAlreadyApprovedException import MedicalAppointmentAlreadyApprovedException
from exceptions.action_already_applied.MedicalAppointmentAlreadyDeclinedException import MedicalAppointmentAlreadyDeclinedException
# Creamos una instancia de Blueprint
# 'cites_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
cites_bp = Blueprint('cites_bp', __name__)

# Definimos las rutas usando el Blueprint
@cites_bp.route('/cites', methods=['POST'])
@needs_auth
@require_role(required_roles=["admin","pacient"])
def add_appointment(*args, **kwargs):
    datos = request.get_json()
    try:
        authorized_user : User = kwargs.get('authorized_user')
        appointment_input_dict = {
            'appointment_date':datos['appointment_date'],
            'id_doctor':datos['id_doctor'],
            'id_patient':datos['id_patient'],
            'id_medical_center':datos['id_medical_center'],
            'motiu':datos['motiu'],
            'id_action_user':authorized_user.id_user,
            'status':MedicalAppointmentStatusEnum.PENDING.value,
        }
        created_appoinment : MedicalAppointment = orm_add_appointment(appointment_input_dict)
        return jsonify({'id_appointment':created_appoinment.id_appointment,
                        'appointment_date':datetime.datetime.fromisoformat(appointment_input_dict['appointment_date']).astimezone(ZoneInfo("Europe/Madrid")),
                        'motiu':created_appoinment.motiu,
                        'medical_appointment_status':{
                            'name':created_appoinment.medical_appointment_status.name,
                        },
                        'id_doctor':created_appoinment.id_doctor,
                        'id_medical_center':created_appoinment.id_medical_center,
                        'id_patient':created_appoinment.id_patient,
                        'id_action_user':created_appoinment.id_action_user}),201
    except (PatientNotFoundException) as e_patient_not_found:
        print(e_patient_not_found.__str__(),file=sys.stderr)
        print(e_patient_not_found.__repr__(),file=sys.stderr)
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
        return jsonify({'message':'Estado de Cita Médica no existe!'}),404
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
@needs_auth
@require_role(required_roles=["admin","secretary"])
def modify_appointment(id,*args, **kwargs):
    datos = request.json()
    try:
        cancelled_medical_appointment : MedicalAppointment = orm_modify_appointment_status(id,datos["action"])
        return jsonify({'id_appointment':cancelled_medical_appointment.id_appointment,
                        'appointment_date':cancelled_medical_appointment.appointment_date,
                        'motiu':cancelled_medical_appointment.motiu,
                        'medical_appointment_status':{
                            'name':cancelled_medical_appointment.medical_appointment_status.name,
                        },
                        'id_doctor':cancelled_medical_appointment.id_doctor,
                        'id_medical_centre':cancelled_medical_appointment.id_medical_centre,
                        'id_patient':cancelled_medical_appointment.id_patient,
                        'id_action_user':cancelled_medical_appointment.id_action_user}),204
    except (MedicalAppointmentAlreadyCancelledException) as e_medical_appointment_already_cancelled:
        print(e_medical_appointment_already_cancelled.__str__(),file=sys.stderr)
        print(e_medical_appointment_already_cancelled.__repr__(),file=sys.stderr)
        return jsonify({'message':'La cita médica ya ha sido cancelada!'}),409
    except (MedicalAppointmentAlreadyDeclinedException) as e_medical_appointment_already_cancelled:
        print(e_medical_appointment_already_cancelled.__str__(),file=sys.stderr)
        print(e_medical_appointment_already_cancelled.__repr__(),file=sys.stderr)
        return jsonify({'message':'La cita médica ya ha sido rechazada!'}),409
    except (MedicalAppointmentAlreadyApprovedException) as e_medical_appointment_already_cancelled:
        print(e_medical_appointment_already_cancelled.__str__(),file=sys.stderr)
        print(e_medical_appointment_already_cancelled.__repr__(),file=sys.stderr)
        return jsonify({'message':'La cita médica ya ha sido aprobada!'}),409
    except (MedicalAppointmentNotFoundException) as e_medical_appointment_not_found:
        print(e_medical_appointment_not_found.__str__(),file=sys.stderr)
        print(e_medical_appointment_not_found.__repr__(),file=sys.stderr)
        return jsonify({'message':'No existe la cita médica que se quiere cancelar!'}),404
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500


# ... (Añadir aquí las rutas POST, PUT, DELETE para citas)