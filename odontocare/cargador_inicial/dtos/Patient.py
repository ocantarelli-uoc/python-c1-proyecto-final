from dtos.User import User
#It defines Data Transfer Object (DTO) for representation of a patient
class Patient:
    def __init__(self,id_patient:int,user:User,name:str,telephone:str,is_active:bool):
        self.id_patient = id_patient
        self.user = user
        self.name = name
        self.telephone = telephone
        self.is_active = is_active

    def describe(self):
        return f"Patient - id_patient: {self.id_patient}, user: {self.user.describe()} , name: {self.name},telephone: {self.telephone} ,." 