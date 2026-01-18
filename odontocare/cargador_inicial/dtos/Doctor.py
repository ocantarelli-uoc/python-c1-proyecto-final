from dtos.User import User
from dtos.MedicalSpeciality import MedicalSpeciality
#It defines Data Transfer Object (DTO) for representation of a doctor
class Doctor: 
    def __init__(self,id_doctor:int,user:User,name:str,medical_speciality:MedicalSpeciality):
        self.id_doctor = id_doctor
        self.user = user
        self.name = name
        self.medical_speciality = medical_speciality

    def describe(self):
        return f"Doctor - id_doctor: {self.id_doctor}, user: {self.user.describe()} , name: {self.name},medical_speciality: {self.medical_speciality.describe()} ,."  