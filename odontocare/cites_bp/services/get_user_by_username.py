from flask import request
import requests
from dtos.User import User
from dtos.UserRole import UserRole

def get_user_by_username(username:str) -> User:
    req = requests.Request('GET', 'http://auth_and_admin_bp:5001/api/v1/users/name/'+username)
    r = req.prepare()
    r.headers['Authorization'] = request.headers.get('Authorization')   
    s = requests.Session()
    rs: requests.Response = s.send(r)
    users_dict = rs.json()
    user_role : UserRole = UserRole(id_user_role=users_dict.user_role.id_user_role,name=users_dict.user_role.name)
    user : User = User(id_user=users_dict.id_user,username=users_dict.username,user_role=user_role)
    return user