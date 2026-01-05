from extensions import db
from models.MedicalAppointment import MedicalAppointment
from models.MedicalAppointmentStatus import MedicalAppointmentStatus
from exceptions.not_found.MedicalAppointmentNotFoundException import MedicalAppointmentNotFoundException
from exceptions.not_found.MedicalAppointmentStatusNotFoundException import MedicalAppointmentStatusNotFoundException
from exceptions.action_already_applied.MedicalAppointmentAlreadyCancelledException import MedicalAppointmentAlreadyCancelledException
from exceptions.action_already_applied.MedicalAppointmentAlreadyApprovedException import MedicalAppointmentAlreadyApprovedException
from exceptions.action_already_applied.MedicalAppointmentAlreadyCreatedException import MedicalAppointmentAlreadyCreatedException
from exceptions.action_already_applied.MedicalAppointmentAlreadyDeclinedException import MedicalAppointmentAlreadyDeclinedException
from enums.MedicalAppointmentStatusEnum import MedicalAppointmentStatusEnum
from enums.MedicalAppointmentActionEnum import MedicalAppointmentActionEnum
from exceptions.action_already_applied.MedicalAppointmentIsCancelledException import MedicalAppointmentIsCancelledException

def modify_appointment_status(id,action) -> MedicalAppointment:
    try:
        if action == MedicalAppointmentActionEnum.CREATE.value:
            status = MedicalAppointmentStatusEnum.PENDING.value
        elif action == MedicalAppointmentActionEnum.CANCEL.value:
            status = MedicalAppointmentStatusEnum.CANCELLED.value
        elif action == MedicalAppointmentActionEnum.APPROVE.value:
            status = MedicalAppointmentStatusEnum.APPROVED.value
        elif action == MedicalAppointmentActionEnum.DECLINE.value:
            status = MedicalAppointmentStatusEnum.DECLINED.value
        else:
            pass
        medical_appointment:MedicalAppointment = MedicalAppointment.query.filter_by(id_medical_appointment=id).first()
        if medical_appointment is None:
            raise MedicalAppointmentNotFoundException()
        medical_appointment_status:MedicalAppointmentStatus = MedicalAppointmentStatus.query.filter_by(name=status).first()
        if medical_appointment_status is None:
            raise MedicalAppointmentStatusNotFoundException()
        if medical_appointment.medical_appointment_status.name == status:
            if status == MedicalAppointmentStatusEnum.CANCELLED.value:
                raise MedicalAppointmentAlreadyCancelledException()
            elif status == MedicalAppointmentStatusEnum.PENDING.value:
                raise MedicalAppointmentAlreadyCreatedException()
            elif status == MedicalAppointmentStatusEnum.APPROVED.value:
                raise MedicalAppointmentAlreadyApprovedException()
            elif status == MedicalAppointmentStatusEnum.DECLINED.value:
                raise MedicalAppointmentAlreadyDeclinedException()
            else:
                pass
        elif medical_appointment.medical_appointment_status.name == MedicalAppointmentStatusEnum.CANCELLED.value and status != MedicalAppointmentStatusEnum.CANCELLED.value:
            raise MedicalAppointmentIsCancelledException()
        else:
            pass
        medical_appointment.medical_appointment_status = medical_appointment_status
        db.session.add(medical_appointment)
        db.session.commit()
        return medical_appointment
    except Exception as e:
        db.session.rollback()
        raise e
