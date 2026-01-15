class UserRole:
    def __init__(self,id_user_role:int,name:str):
        self.id_user_role = id_user_role
        self.name = name
    
    def describe(self):
        return f"UserRole - id_user_role: {self.id_user_role}, name: {self.name}." 