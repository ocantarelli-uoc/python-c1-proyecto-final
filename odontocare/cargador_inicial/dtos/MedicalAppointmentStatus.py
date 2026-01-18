#It defines Data Transfer Object (DTO) for representation of a medical appointment status
class MedicalAppointmentStatus:
    def __init__(self,id_medical_status:int,name:str):
        self.id_medical_status = id_medical_status
        self.name = name
    
    def describe(self):
        return f"MedicalAppointmentStatus - id_medical_status: {self.id_medical_status}, name: {self.name}" 