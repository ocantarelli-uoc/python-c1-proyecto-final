import jwt
import sys
from functools import wraps
from flask import Flask, jsonify, request
from models.User import User
from models.UserRole import UserRole
# Decorador personalizado para verificar el rol
def require_role(required_roles:list[str]):
    def decorador_interno(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                #print(*args, file=sys.stderr, **kwargs)
                # 2. Verificación del permiso
                authorized_user : User = kwargs.get('authorized_user')
                if authorized_user != None:
                    user_role : UserRole = authorized_user.user_role
                    if user_role == None or user_role.name not in required_roles:
                        return jsonify({'message': 'Permiso denegado'}), 403

            except Exception as e:
                print(e.__str__(),file=sys.stderr)
                print(e.__repr__(),file=sys.stderr)
                return jsonify({'message': 'Ha ocurrido algún error al verificar rol.'}), 500

            return f(*args, **kwargs)
        return wrapper
    return decorador_interno