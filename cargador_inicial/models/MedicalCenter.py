from models.Address import Address
class MedicalCenter:
    def __init__(self,id_medical_center:int,address:Address,name:str):
        self.id_medical_center = id_medical_center
        self.address = address
        self.name = name
    
    def describe(self):
        return f"MedicalCenter - id_medical_center: {self.id_medical_center}, address: {self.address.describe()},name:{self.name}." 