from flask import Blueprint, jsonify, request
import sys
from models.UserRole import UserRole
from admin_bp.users.services.get_user_by_id import get_user_by_id as orm_get_user_by_id
from admin_bp.users.services.get_user_by_username import get_user_by_username as orm_get_user_by_username
from admin_bp.users.services.create_user import create_user
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role
from admin_bp.exceptions.already_exists.UserAlreadyExistsException import UserAlreadyExistsException
from admin_bp.users.services.list_users import list_users as orm_list_users
from models import User
from admin_bp.exceptions.not_found.UserNotFoundException import UserNotFoundException
from admin_bp.exceptions.authorization.UnauthorizedRoleException import UnauthorizedRoleException
# Creamos una instancia de Blueprint
# "users_bp" es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
users_bp = Blueprint("users_bp", __name__)

# Definimos las rutas usando el Blueprint
@users_bp.route("/admin/usuaris", methods=["POST"])
@needs_auth
@require_role(required_roles=["admin"])
#It defines the endpoint for adding a user
def add_user(*args, **kwargs):
    datos = request.get_json()
    try:
        #It tries to get user by name
        existing_user:User = orm_get_user_by_username(datos["username"])
        #It controls if the user already exists
        if existing_user is not None:
            raise UserAlreadyExistsException()
        #It creates the user
        createdUser = create_user({
            "username":datos["username"],
            "password":datos["password"],
            "user_role":datos["user_role"]
        },user_role_str=None)
        user = orm_get_user_by_id(createdUser.id_user)
        if user is None:
            raise UserNotFoundException()
        #It returns the created user in json format
        return jsonify({"id_user": user.id_user, "username": user.username,
                        "user_role":{
                            "id_user_role":user.user_role.id_user_role,
                            "name":user.user_role.name,
                        }})
    #It captures if the user already exists
    except UserAlreadyExistsException as e_user_already_exists:
        print(e_user_already_exists.__str__(),file=sys.stderr)
        print(e_user_already_exists.__repr__(),file=sys.stderr)
        return jsonify({"message":"Usuario "+datos["username"]+" ya existe."}),409
    #It captures if created user hasn't been found
    except UserNotFoundException as e_user_not_found:
        print(e_user_not_found.__str__(),file=sys.stderr)
        print(e_user_not_found.__repr__(),file=sys.stderr)
        return jsonify({"message":"Usuario "+datos["username"]+" creado no se ha encontrado."}),404
    #It captures if an error has ocurred
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500
    
# Definimos las rutas usando el Blueprint
@users_bp.route("/admin/usuaris", methods=["GET"])
@needs_auth
@require_role(required_roles=["admin"])
#It defines the endpoint for getting users
def list_users(*args, **kwargs):
    try:
        #It gets the users from repository from database
        users = orm_list_users()
        #It returns the users as list in dictionary format for returning as json
        user_list = [{"id": u.id_user, "name": u.username, "role": u.user_role.name} for u in users]
        return jsonify(user_list)
    #It controls if an error has ocurred
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500

@users_bp.route("/admin/usuaris/<int:id>", methods=["GET"])
@needs_auth
@require_role(required_roles=["admin"])
#It defines the endpoint for getting user by id
def get_user_by_id(id,*args, **kwargs):
    try:
        #It gets the user by id from repository from database
        user = orm_get_user_by_id(id)
        #It controls if the user hasn't been found
        if user is None:
            raise UserNotFoundException()
        #It returns the user in dictionary format for returning as json
        user_dict = [{"id": user.id_user, "username": user.username, "role": user.user_role.name}]
        return jsonify(user_dict)
    #It captures if the user hasn't been found
    except (UserNotFoundException) as e_user_not_found:
        print(e_user_not_found.__str__(),file=sys.stderr)
        print(e_user_not_found.__repr__(),file=sys.stderr)
        return jsonify({"message":"Usuario no encontrado!"}),404
    #It captures if an error has ocurred
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500

@users_bp.route("/admin/usuaris/name/<string:username>", methods=["GET"])
@needs_auth
@require_role(required_roles=["admin","secretary","patient","doctor"])
#It defines the endpoint for getting user role by username
def get_user_by_username(username,*args, **kwargs):
    try:
        #It controls whether it can get user by username or not
        user = None
        authorized_user : User = kwargs.get("authorized_user")
        if authorized_user is not None:
            user_role : UserRole = authorized_user.user_role
            if user_role is None or user_role.name not in ["admin"] and authorized_user.username != username:
                raise UnauthorizedRoleException()
            else:
                #It gets the user role by id from repository from database
                user : User = orm_get_user_by_username(username)
        #It controls if the user hasn't been found
        if user is None:
            raise UserNotFoundException()
        #It returns the user in dictionary format for returning as json
        user_dict = [{"id_user": user.id_user, "username": user.username, 
            "user_role":{
                "id_user_role":user.user_role.id_user_role,
                "name":user.user_role.name,
            }
          }]
        return jsonify(user_dict)
    #It captures if the user isn't authorized for getting this user by username
    except (UnauthorizedRoleException) as e_unauthorized_user:
        print(e_unauthorized_user.__str__(),file=sys.stderr)
        print(e_unauthorized_user.__repr__(),file=sys.stderr)
        return jsonify({"message":"No tienes permiso para consultar este usuario!"}),403
    #It captures if the user hasn't been found
    except (UserNotFoundException) as e_user_not_found:
        print(e_user_not_found.__str__(),file=sys.stderr)
        print(e_user_not_found.__repr__(),file=sys.stderr)
        return jsonify({"message":"Usuario no encontrado!"}),404
    #It captures if an error has ocurred
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({"message":"Ha ocurrido algún error!"}),500