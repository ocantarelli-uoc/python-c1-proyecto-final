import jwt
from functools import wraps
from flask import Flask, jsonify, request
from dotenv import dotenv_values
import app
from admin_bp.users.services.get_user_by_username import get_user_by_username
# Decorador personalizado para la autenticación
def needs_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
    # 1. Validación del token
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'mensaje': 'Token no proporcionado'}), 401
            
        token = auth_header.split(" ")[1]
        try:
            dotenv_config_values = dotenv_values('.env')
            payload = jwt.decode(token, dotenv_config_values['SECRET_KEY'], algorithms=['HS256'])
            payload_user = payload['sub']
            user = get_user_by_username(payload_user)
            # 2. Verificación del usuario
            if user != None:
                kwargs['authorized_user'] = user
                return f(*args, **kwargs)
            else:
                return jsonify({'mensaje': 'Usuario no encontrado'}), 404

        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
                return jsonify({'mensaje': 'Token inválido'}), 401
            
    return wrapper