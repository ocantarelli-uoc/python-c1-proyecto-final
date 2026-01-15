from models.UserRole import UserRole

class User:
    def __init__(self,id_user:int,username:str,password:str,user_role:UserRole):
        self.id_user = id_user
        self.username = username
        self.password = password
        self.user_role = user_role

    def describe(self):
        return f"User - id_user: {self.id_user}, username: {self.username},password:{self.password},user_role:{self.user_role.describe()}." 