from dtos.Address import Address
class MedicalCenter:
    def __init__(self,id_medical_center:int,address:Address,name:str):
        self.id_medical_center = id_medical_center
        self.address = address
        self.name = name