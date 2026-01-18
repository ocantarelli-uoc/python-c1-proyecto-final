#It defines Data Transfer Object (DTO) for representation of a medical speciality
class MedicalSpeciality:
    def __init__(self,id_medical_speciality:int,name:str):
        self.id_medical_speciality = id_medical_speciality
        self.name = name
    
    def describe(self):
        return f"MedicalSpeciality - id_medical_speciality: {self.id_medical_speciality}, name: {self.name}." 