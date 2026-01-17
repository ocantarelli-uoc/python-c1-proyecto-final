import jwt
from functools import wraps
from flask import Flask, jsonify, request
from dotenv import dotenv_values
from admin_bp.users.services.get_user_by_username import get_user_by_username
# Personalized Decorator for the authentication
def needs_auth(f):
    #It defines the wrapper for personalized decorator
    @wraps(f)
    def wrapper(*args, **kwargs):
    # It gets the authorization header from request
        auth_header = request.headers.get('Authorization')
        #If authorization header value is None (null)
        if not auth_header:
            #It returns unauthorized error message with personalized message
            return jsonify({'message': 'Token no proporcionado'}), 401
        #It split the token by space(" ") and it gets the token value (like jwt it's: "Bearer "+token) and it gets the second part avoiding Bearer part
        token = auth_header.split(" ")[1]
        try:
            #It gets dotenv configuration values
            dotenv_config_values = dotenv_values('.env')
            #It decodes the JWT token with the secret key with HS256 algorithm
            payload = jwt.decode(token, dotenv_config_values['SECRET_KEY'], algorithms=['HS256'])
             #It returns the payload from the token 
            payload_user = payload['sub']
            #It returns the user by username given the payload user
            user = get_user_by_username(payload_user)
            # It checks if the user is not None (null)
            if user is not None:
                #It assigns authorized_user got from payload_user through kwargs
                kwargs['authorized_user'] = user
                #It returns with the endpoint method, which it's expecting to be called later
                return f(*args, **kwargs)
            else:
                #It returns a Not Found Http REST error with personalized message
                return jsonify({'message': 'Usuario no encontrado'}), 404

        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
                #It returns an unauthorized Http REST error with invalid token message
                return jsonify({'message': 'Token inválido'}), 401
    #It returns the wrapper
    return wrapper