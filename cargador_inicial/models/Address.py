class Address: 
    def __init__(self,id_address:int,street:str,city:str):
        self.id_address = id_address
        self.street = street
        self.city = city

    def describe(self):
        return f"Address - id_address: {self.id_address}, street: {self.street} , city: {self.city},."  