from datetime import datetime

from cargador_inicial.dtos.MedicalAppointmentStatus import MedicalAppointmentStatus
from cargador_inicial.dtos.Doctor import Doctor
from cargador_inicial.dtos.Patient import Patient
from cargador_inicial.dtos.User import User
class MedicalAppointment:
    def __init__(self,id_medical_appointment:int,appointment_date:datetime,
                 motiu:str,medical_status:MedicalAppointmentStatus,
                 id_doctor:int,id_patient:int,id_action_user:int,
                 id_medical_center:int):
        self.id_medical_appointment = id_medical_appointment
        self.appointment_date = appointment_date
        self.motiu = motiu
        self.medical_status = medical_status
        self.doctor = id_doctor
        self.patient = id_patient
        self.action_user = id_action_user
        self.id_medical_appointment = id_medical_appointment