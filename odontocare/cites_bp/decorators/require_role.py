import jwt
import sys
from functools import wraps
from flask import Flask, jsonify, request
from dtos.User import User
from dtos.UserRole import UserRole
# Personalized Decorator for the authorization (role authorization)
def require_role(required_roles:list[str]):
    #It defines the internal decorator
    def iternal_decorator(f):
        #It defines the wrapper
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                #print(*args, file=sys.stderr, **kwargs)
                # It gets the authorization header from request
                authorized_user : User = kwargs.get('authorized_user')
                # It checks if the authorized user is not None (null)
                if authorized_user is not None:
                    #It returns the user role (user_role) from authorized user (authorized_user)
                    user_role : UserRole = authorized_user.user_role
                    #It checks if user role (user_role) is None (null) or if its name it isn't on required roles (required_roles)
                    if user_role is None or user_role.name not in required_roles:
                        #It sends an HTTP REST code for unauthorized (forbidden) error
                        return jsonify({'message': 'Permiso denegado'}), 403
            #It captures generic exception
            except Exception as e:
                print(e.__str__(),file=sys.stderr)
                print(e.__repr__(),file=sys.stderr)
                #It sends HTTP REST code for internal server error message
                return jsonify({'message': 'Ha ocurrido algún error al verificar rol.'}), 500
            #It returns the function which its' expected to be called later after decorator executation
            return f(*args, **kwargs)
        #It returns the wrapper
        return wrapper
    #It returns the internal decorator
    return iternal_decorator