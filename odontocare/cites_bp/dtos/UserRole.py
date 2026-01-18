#It defines Data Transfer Object (DTO) for representation of a user role
class UserRole:
    def __init__(self,id_user_role:int,name:str):
        self.id_user_role = id_user_role
        self.name = name