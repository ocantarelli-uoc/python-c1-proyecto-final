import jwt
from functools import wraps
from flask import Flask, jsonify, request
from decorators.needs_authorization import needs_auth
from models.User import User
from models.UserRole import UserRole
# Decorador personalizado para verificar el rol
def require_role(required_roles:list[str]):
    def decorador_interno(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # 1. Validación del token
            try:
                # 2. Verificación del permiso
                authorized_user : User = kwargs.get('authorized_user')
                if authorized_user != None:
                    user_role : UserRole = authorized_user.role
                    if user_role == None or user_role.name not in required_roles:
                        return jsonify({'mensaje': 'Permiso denegado'}), 403

            except (Exception):
                return jsonify({'mensaje': 'Ha ocurrido algún error al verificar rol.'}), 500

            return f(*args, **kwargs)
        return wrapper
    return decorador_interno