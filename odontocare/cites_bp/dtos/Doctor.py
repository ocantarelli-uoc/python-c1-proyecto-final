from dtos.User import User
from dtos.MedicalSpeciality import MedicalSpeciality
class Doctor: 
    def __init__(self,id_patient:int,user:User,name:str,medical_speciality:MedicalSpeciality):
        self.id_patient = id_patient
        self.user = user
        self.name = name
        self.medical_speciality = medical_speciality