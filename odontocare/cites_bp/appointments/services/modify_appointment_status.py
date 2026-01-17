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
from exceptions.invalid.MedicalAppointmentInvalidActionException import MedicalAppointmentInvalidActionException
from exceptions.action_already_applied.MedicalAppointmentIsApprovedException import MedicalAppointmentIsApprovedException
from exceptions.action_already_applied.MedicalAppointmentIsDeclinedException import MedicalAppointmentIsDeclinedException

def modify_appointment_status(id,action) -> MedicalAppointment:
    try:
        #It checks for which status to modify the appointment through the specified action
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
        #It gets the medical appoinment by id
        medical_appointment:MedicalAppointment = MedicalAppointment.query.filter_by(id_medical_appointment=id).first()
        #It checks if the medical appointment is not found
        if medical_appointment is None:
            #It throws the medical appointment not found exception
            raise MedicalAppointmentNotFoundException()
        #It gets the medical appointment status by name
        medical_appointment_status:MedicalAppointmentStatus = MedicalAppointmentStatus.query.filter_by(name=status).first()
        #It checks if medical appointment status is None
        if medical_appointment_status is None:
            #It throws the medical appointment status not found
            raise MedicalAppointmentStatusNotFoundException()
        #It checks if the medical appointment status from appointment it's the same to assign
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
                raise MedicalAppointmentInvalidActionException()
        else:
            #If it's not the same the medical appointment status than status to assign, it checks if the appointment has been cancelled
            if medical_appointment.medical_appointment_status.name == MedicalAppointmentStatusEnum.CANCELLED.value and status != MedicalAppointmentStatusEnum.CANCELLED.value:
                raise MedicalAppointmentIsCancelledException()
            #If it's not the same the medical appointment status than status to assign, it checks if the appointment has been approved
            elif medical_appointment.medical_appointment_status.name == MedicalAppointmentStatusEnum.APPROVED.value and status == MedicalAppointmentStatusEnum.DECLINED.value:
                raise MedicalAppointmentIsApprovedException()
            #If it's not the same the medical appointment status than status to assign, it checks if the appointment has been declined
            elif medical_appointment.medical_appointment_status.name == MedicalAppointmentStatusEnum.DECLINED.value and status == MedicalAppointmentStatusEnum.APPROVED.value:
                raise MedicalAppointmentIsDeclinedException()
            else:
                pass
        #It modify appointment status to the status that it's intended to be assigned
        medical_appointment.medical_appointment_status = medical_appointment_status
        #It saves the changes to database through ORM
        db.session.add(medical_appointment)
        #It commits the changes
        db.session.commit()
        #It returns the modified appointment
        return medical_appointment
    #It captures the generic exception
    except Exception as e:
        #It rollback the changes
        db.session.rollback()
        #It throws the generic exception
        raise e
