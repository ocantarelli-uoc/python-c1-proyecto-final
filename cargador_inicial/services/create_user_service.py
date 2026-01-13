import sys
from flask import request
import requests
from dtos.Token import Token
from dtos.User import User
from dtos.UserRole import UserRole

def create_user(user:User,token:Token) -> User:
    body_payload:dict={
        "username":user.username,
        "password":user.password,
        "user_role":user.user_role.name
    }
    req = requests.post('http://localhost:5001/api/v1/admin/usuaris',json=body_payload)
    r = req.prepare()
    r.headers['Authorization'] = token.token
    r.headers['Content-Type'] = 'application/json'
    s = requests.Session()
    rs: requests.Response = s.send(r)
    user_list = rs.json()
    user : User = User(id_user=user_list[0]['id_user'],
                      username=user_list[0]['username'],
                       password=user_list[0]['password'],
                        user_role=UserRole(
                            id_user_role=user_list[0]['user_role']['id_user_role'],
                            name=user_list[0]['user_role']['name']
                        ) 
                 )
    return user