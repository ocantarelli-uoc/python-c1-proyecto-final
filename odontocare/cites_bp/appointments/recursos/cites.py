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
from exceptions.action_already_applied.MedicalAppointmentIsCancelledException import MedicalAppointmentIsCancelledException
from exceptions.action_already_applied.MedicalAppointmentIsApprovedException import MedicalAppointmentIsApprovedException
from exceptions.action_already_applied.MedicalAppointmentIsDeclinedException import MedicalAppointmentIsDeclinedException
from appointments.services.get_medical_appointment_by_id import get_medical_appointment_by_id as orm_get_medical_appointment_by_id
from appointments.services.get_doctor_by_id import get_doctor_by_id as orm_get_doctor_by_id
from appointments.services.get_appointments_by_patient import get_appointments_by_patient
from appointments.services.get_patient_by_id import get_patient_by_id as orm_get_patient_by_id
from dtos.Doctor import Doctor
from appointments.services.get_appointments_by_doctor import get_appointments_by_doctor
from dtos.Patient import Patient
from appointments.services.get_appointments_by_patient import get_appointments_by_patient
from dtos.MedicalCenter import MedicalCenter
from appointments.services.get_medical_center_by_id import get_medical_center_by_id as orm_get_medical_center_by_id
from appointments.services.get_appointments_by_medical_center import get_appointments_by_medical_center as get_appointments_by_medical_center
from models.MedicalAppointmentStatus import MedicalAppointmentStatus
from appointment_statuses.services.get_medical_appointment_status_by_id import get_medical_appointment_status_by_id as orm_get_medical_appointment_status_by_id
from appointments.services.get_appointments_by_status import get_appointments_by_status
from appointments.services.get_appointments_by_date import get_appointments_by_date
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
        return jsonify({'id_medical_appointment':created_appoinment.id_medical_appointment,
                        'appointment_date':datetime.datetime.fromisoformat(str(created_appoinment.appointment_date)).astimezone(ZoneInfo("Europe/Madrid")).isoformat(),
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
    authorized_user : User = kwargs.get('authorized_user')
    filter_by = request.args.get('filter_by')
    filter_value = request.args.get('filter_value')
    if filter_by == "doctor":
        if authorized_user.user_role.name=="doctor":
            doctor_id = authorized_user.id_user
        else:
         doctor_id = filter_value
        doctor : Doctor = orm_get_doctor_by_id(doctor_id)
        require_role(required_roles=["admin","doctor"])
        appointments : list[MedicalAppointment] = get_appointments_by_doctor(doctor)
    if filter_by == "patient":
        patient : Patient = orm_get_patient_by_id(filter_value)
        require_role(required_roles=["admin"])
        appointments : list[MedicalAppointment] = get_appointments_by_patient(
            patient
        )
    if filter_by == "center":
        medical_center : MedicalCenter = orm_get_medical_center_by_id(filter_value)
        require_role(required_roles=["admin"])
        appointments : list[MedicalAppointment] = get_appointments_by_medical_center(
            medical_center
        )
    if filter_by == "status":
        medical_status : MedicalAppointmentStatus = orm_get_medical_appointment_status_by_id(filter_value)
        require_role(required_roles=["admin"])
        appointments : list[MedicalAppointment] = get_appointments_by_status(
            medical_status
        )
    if filter_by == "data":
        medical_status : MedicalAppointmentStatus = orm_get_medical_appointment_status_by_id(filter_value)
        require_role(required_roles=["admin","secretary"])
        appointments : list[MedicalAppointment] = get_appointments_by_date(
        datetime.datetime.fromisoformat(str(filter_value)))
    
    medical_appointments_list = [{'id_medical_appointment':m_a.id_medical_appointment,
                        'appointment_date':datetime.datetime.fromisoformat(str(m_a.appointment_date)).astimezone(ZoneInfo("Europe/Madrid")).isoformat(),
                        'motiu':m_a.motiu,
                        'medical_appointment_status':{
                            'name':m_a.medical_appointment_status.name,
                        },
                        'id_doctor':m_a.id_doctor,
                        'id_medical_center':m_a.id_medical_center,
                        'id_patient':m_a.id_patient,
                        'id_action_user':m_a.id_action_user} for m_a in appointments]
    return jsonify(medical_appointments_list)


@cites_bp.route('/cites/<int:id>', methods=['GET'])
@needs_auth
@require_role(required_roles=["admin","pacient"])
def get_appointment_by_id(id,*args,**kwargs):
    try:
        appointment : MedicalAppointment = orm_get_medical_appointment_by_id(id)
        if appointment is None:
            raise MedicalAppointmentNotFoundException()
        return jsonify({'id_medical_appointment':appointment.id_medical_appointment,
                        'appointment_date':datetime.datetime.fromisoformat(str(appointment.appointment_date)).astimezone(ZoneInfo("Europe/Madrid")).isoformat(),
                        'motiu':appointment.motiu,
                        'medical_appointment_status':{
                            'name':appointment.medical_appointment_status.name,
                        },
                        'id_doctor':appointment.id_doctor,
                        'id_medical_center':appointment.id_medical_center,
                        'id_patient':appointment.id_patient,
                        'id_action_user':appointment.id_action_user}),200
    except (MedicalAppointmentNotFoundException) as e_medical_appointment_not_found:
        print(e_medical_appointment_not_found.__str__(),file=sys.stderr)
        print(e_medical_appointment_not_found.__repr__(),file=sys.stderr)
        return jsonify({'message':'Cita Médica no encontrada!'}),404
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

@cites_bp.route('/cites/<int:id>', methods=['PUT'])
@needs_auth
@require_role(required_roles=["admin","secretary"])
def modify_appointment(id,*args, **kwargs):
    datos = request.get_json()
    try:
        modified_medical_appointment : MedicalAppointment = orm_modify_appointment_status(id,datos["action"])
        modified_medical_appointment_dict : dict = {
                        'id_medical_appointment':modified_medical_appointment.id_medical_appointment,
                        'appointment_date':datetime.datetime.fromisoformat(str(modified_medical_appointment.appointment_date)).astimezone(ZoneInfo("Europe/Madrid")).isoformat(),
                        'motiu':modified_medical_appointment.motiu,
                        'medical_appointment_status':{
                            'name':modified_medical_appointment.medical_appointment_status.name,
                        },
                        'id_doctor':modified_medical_appointment.id_doctor,
                        'id_medical_center':modified_medical_appointment.id_medical_center,
                        'id_patient':modified_medical_appointment.id_patient,
                        'id_action_user':modified_medical_appointment.id_action_user}
        return jsonify(modified_medical_appointment_dict),200
    except (MedicalAppointmentAlreadyCancelledException) as e_medical_appointment_already_cancelled:
        print(e_medical_appointment_already_cancelled.__str__(),file=sys.stderr)
        print(e_medical_appointment_already_cancelled.__repr__(),file=sys.stderr)
        return jsonify({'message':'La cita médica ya ha sido cancelada!'}),409
    except (MedicalAppointmentIsCancelledException) as e_medical_appointment_is_cancelled:
        print(e_medical_appointment_is_cancelled.__str__(),file=sys.stderr)
        print(e_medical_appointment_is_cancelled.__repr__(),file=sys.stderr)
        return jsonify({'message':'La cita médica fue cancelada previamente!'}),409
    except (MedicalAppointmentIsDeclinedException) as e_medical_appointment_is_declined:
        print(e_medical_appointment_is_declined.__str__(),file=sys.stderr)
        print(e_medical_appointment_is_declined.__repr__(),file=sys.stderr)
        return jsonify({'message':'La cita médica fue rechazada previamente!'}),409
    except (MedicalAppointmentIsApprovedException) as e_medical_appointment_is_approved:
        print(e_medical_appointment_is_approved.__str__(),file=sys.stderr)
        print(e_medical_appointment_is_approved.__repr__(),file=sys.stderr)
        return jsonify({'message':'La cita médica fue aprobada previamente!'}),409
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