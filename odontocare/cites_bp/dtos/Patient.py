from dtos.User import User
class Patient:
    def __init__(self,id_patient:int,user:User,name:str,telephone:str):
        self.id_patient = id_patient
        self.user = user
        self.name = name
        self.telephone = telephone