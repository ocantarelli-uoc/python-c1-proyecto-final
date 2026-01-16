from datetime import datetime

from models.MedicalAppointmentStatus import MedicalAppointmentStatus
from models.Doctor import Doctor
from models.Patient import Patient
from models.User import User
class MedicalAppointment:
    def __init__(self,id_medical_appointment:int,appointment_date:datetime,
                 motiu:str,medical_appointment_status:MedicalAppointmentStatus,
                 id_doctor:int,id_patient:int,id_action_user:int,
                 id_medical_center:int):
        self.id_medical_appointment = id_medical_appointment
        self.appointment_date = appointment_date
        self.motiu = motiu
        self.medical_appointment_status = medical_appointment_status
        self.id_doctor = id_doctor
        self.id_patient = id_patient
        self.id_action_user = id_action_user
        self.id_medical_center = id_medical_center
        
    def describe(self):
        return f"MedicalAppointment - id_medical_appointment: {self.id_medical_appointment}, appointment_date: {self.appointment_date},motiu:{self.motiu},medical_status:{self.medical_appointment_status.describe()},id_doctor:{self.id_doctor},id_patient:{self.id_patient},id_action_user:{self.id_action_user},id_medical_center:{self.id_medical_center} ." 