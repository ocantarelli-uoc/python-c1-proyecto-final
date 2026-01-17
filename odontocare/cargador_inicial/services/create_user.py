from flask import request
import requests
from models.Token import Token
from models.UserRole import UserRole
from models.User import User

def create_user(user:User,token:Token) -> User:
        body_payload:dict={
            "username":user.username,
            "password":user.password,
            "user_role":user.user_role.name
        }
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/usuaris',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = "Bearer " + token.token
        r.headers['Content-Type'] = 'application/json'
        s = requests.Session()
        rs: requests.Response = s.send(r)
        user_list = rs.json()
        user : User = User(id_user=user_list['id_user'],
                        username=user_list['username'],
                        password=None,
                            user_role=UserRole(
                                id_user_role=user_list['user_role']['id_user_role'],
                                name=user_list['user_role']['name']
                            ) 
                    )
        return user