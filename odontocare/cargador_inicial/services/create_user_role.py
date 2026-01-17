from flask import request
import requests
from models.Token import Token
from models.UserRole import UserRole


def create_user_role(user_role:UserRole,token:Token) -> UserRole:
        body_payload:dict={
            "role_name":user_role.name,
        }
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/rols_usuaris',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = "Bearer " + token.token
        r.headers['Content-Type'] = 'application/json'
        s = requests.Session()
        rs: requests.Response = s.send(r)
        user_role_list = rs.json()
        user_role : UserRole = UserRole(
            id_user_role=user_role_list['id_user_role'],
            name=user_role_list['name']
        )
        return user_role