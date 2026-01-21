from flask import Blueprint, jsonify, request
import sys
import jwt
from dotenv import dotenv_values
import datetime
from admin_bp.users.services.get_user_by_username import get_user_by_username
from models.User import User
from auth_bp.services.hash_password import check_password

# Creamos una instancia de Blueprint
# "auth_bp" es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
auth_bp = Blueprint("auth_bp", __name__)

# Definimos las rutas usando el Blueprint
@auth_bp.route("/auth/login", methods=["POST"])
#It defines the endpoint for login user
def login_user():
    try:
        # It loads dotenv values
        config_dotenv_values = dotenv_values(".env")
        credentials = request.get_json()
        given_user = credentials.get("user")
        plain_password = credentials.get("password")
        #It gets user by username
        user:User = get_user_by_username(given_user)

        #It checks if user is not found:
        if user is None:
            return jsonify({"message": "Usuario no encontrado!"}),404

        #It checks if the username and password are correct
        if given_user == user.username and check_password(user.password,plain_password):
            # It generates the JWT Token
            payload = {
                "sub": user.username,
                "iat": datetime.datetime.now(datetime.timezone.utc),
                "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)
            }
            token = jwt.encode(payload, config_dotenv_values["SECRET_KEY"])
            #It returns the Token
            return jsonify({"token": token})
        else:
            return jsonify({"message": "Credenciales de Usuario Inválidas!!"}),401
    #It controls if an error has ocurred
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500