from models.User import User
from models.MedicalSpeciality import MedicalSpeciality
class Doctor: 
    def __init__(self,id_doctor:int,user:User,name:str,medical_speciality:MedicalSpeciality):
        self.id_doctor = id_doctor
        self.user = user
        self.name = name
        self.medical_speciality = medical_speciality

    def describe(self):
        return f"Doctor - id_doctor: {self.id_doctor}, user: {self.user.describe()} , name: {self.name},medical_speciality: {self.medical_speciality.describe()} ,."  