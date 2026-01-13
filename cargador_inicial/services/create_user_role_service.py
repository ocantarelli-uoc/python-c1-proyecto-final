import sys
from flask import request
import requests
from dtos.Token import Token
from dtos.UserRole import UserRole

def create_user_role(user_role:UserRole,token:Token) -> UserRole:
    body_payload:dict={
        "role_name":user_role.name,
    }
    req = requests.post('http://localhost:5001/api/v1/admin/rols_usuaris',json=body_payload)
    r = req.prepare()
    r.headers['Authorization'] = token.token
    r.headers['Content-Type'] = 'application/json'
    s = requests.Session()
    rs: requests.Response = s.send(r)
    user_role_list = rs.json()
    user_role : UserRole = UserRole(
        id_user_role=user_role_list[0]['id_user_role'],
        name=user_role_list[0]['name']
    )
    return user_role
