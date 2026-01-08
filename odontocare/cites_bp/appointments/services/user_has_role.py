import jwt
import sys
from functools import wraps
from flask import Flask, jsonify, request
from dtos.User import User
from dtos.UserRole import UserRole
# Decorador personalizado para verificar el rol
def user_has_role(required_roles:list[str],*args, **kwargs):
    try:
        authorized_user : User = kwargs.get('authorized_user')
        if authorized_user != None:
         user_role : UserRole = authorized_user.user_role
        if user_role is None or user_role.name not in required_roles:
            return {'status_code':403}

    except Exception as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return {'status_code':500}
    return {'status_code':200}