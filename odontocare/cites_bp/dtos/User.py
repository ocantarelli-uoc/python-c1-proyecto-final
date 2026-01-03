from dtos.UserRole import UserRole

class User:
    def __init__(self,id_user:int,username:str,user_role:UserRole):
        self.id_user = id_user
        self.username = username
        self.user_role = user_role