import sys
from flask import request
import requests
from dtos.User import User
from dtos.UserRole import UserRole

def get_user_by_username(username:str) -> User:
    print(username,file=sys.stderr)
    req = requests.Request('GET', 'http://auth_and_admin_bp:5001/api/v1/admin/usuaris/name/'+str(username))
    r = req.prepare()
    r.headers['Authorization'] = request.headers.get('Authorization')
    r.headers['Content-Type'] = 'application/json'   
    s = requests.Session()
    rs: requests.Response = s.send(r)
    users_list = rs.json()
    user_role : UserRole = UserRole(id_user_role=users_list[0]['user_role']['id_user_role'],name=users_list[0]['user_role']['name'])
    user : User = User(id_user=users_list[0]['id_user'],username=users_list[0]['username'],user_role=user_role)
    return user