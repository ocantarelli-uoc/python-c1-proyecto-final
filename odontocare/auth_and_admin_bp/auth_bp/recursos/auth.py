from flask import Blueprint, jsonify, request
import sys
import jwt
from dotenv import dotenv_values
import datetime
from admin_bp.users.services.get_user_by_username import get_user_by_username
from models.User import User
from auth_bp.services.hash_password import check_password

# Creamos una instancia de Blueprint
# 'auth_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
auth_bp = Blueprint('auth_bp', __name__)

# Definimos las rutas usando el Blueprint
@auth_bp.route('/auth/login', methods=['POST'])
def login_user():
    try:
        # It loads dotenv values
        config_dotenv_values = dotenv_values(".env")
        credentials = request.get_json()
        given_user = credentials.get('user')
        plain_password = credentials.get('password')
        user:User = get_user_by_username(given_user)

        if given_user == user.username and check_password(user.password,plain_password):
            # Generamos el token JWT
            payload = {
                'sub': user.username,
                'iat': datetime.datetime.now(datetime.timezone.utc),
                'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)
            }
            token = jwt.encode(payload, config_dotenv_values['SECRET_KEY'])
            return jsonify({'token': token})
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

# ... (Añadir aquí las rutas POST, PUT, DELETE para autenticación)