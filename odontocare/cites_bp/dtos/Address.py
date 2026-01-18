#It defines Data Transfer Object (DTO) for representation of an address
class Address: 
    def __init__(self,id_address:int,street:str,city:str):
        self.id_address = id_address
        self.street = street
        self.city = city