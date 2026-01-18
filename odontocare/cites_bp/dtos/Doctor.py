from dtos.User import User
from dtos.MedicalSpeciality import MedicalSpeciality
#It defines Data Transfer Object (DTO) for representation of an doctor
class Doctor: 
    def __init__(self,id_doctor:int,user:User,name:str,medical_speciality:MedicalSpeciality):
        self.id_doctor = id_doctor
        self.user = user
        self.name = name
        self.medical_speciality = medical_speciality