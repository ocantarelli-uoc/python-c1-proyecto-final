from flask import Blueprint, jsonify, request
import sys
from admin_bp.users.services.get_user_by_id import get_user_by_id as orm_get_user_by_id
from admin_bp.users.services.get_user_by_username import get_user_by_username as orm_get_user_by_username
from admin_bp.users.services.create_user import create_user
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role
from admin_bp.exceptions.already_exists.UserAlreadyExistsException import UserAlreadyExistsException
from admin_bp.users.services.list_users import list_users as orm_list_users
from models import User
from admin_bp.exceptions.not_found.UserNotFoundException import UserNotFoundException

# Creamos una instancia de Blueprint
# 'users_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
users_bp = Blueprint('users_bp', __name__)

# Definimos las rutas usando el Blueprint
@users_bp.route('/admin/usuaris', methods=['POST'])
@needs_auth
@require_role(required_roles=["admin"])
def add_user(*args, **kwargs):
    datos = request.get_json()
    try:
        existing_user:User = orm_get_user_by_username(datos['username'])
        if existing_user != None:
            raise UserAlreadyExistsException()
        createdUser = create_user({
            'username':datos['username'],
            'password':datos['password'],
            'user_role':datos['user_role']
        },user_role_str=None)
        user = orm_get_user_by_id(createdUser.id_user)
        if user == None:
            raise UserNotFoundException()
        return jsonify({'id': user.id_user, 'username': user.username})
    except UserAlreadyExistsException as e_user_already_exists:
        print(e_user_already_exists.__str__(),file=sys.stderr)
        print(e_user_already_exists.__repr__(),file=sys.stderr)
        return jsonify({'message':'Usuario '+datos['username']+' ya existe.'}),409
    except UserNotFoundException as e_user_not_found:
        print(e_user_not_found.__str__(),file=sys.stderr)
        print(e_user_not_found.__repr__(),file=sys.stderr)
        return jsonify({'message':'Usuario '+datos['username']+' creado no se ha encontrado.'}),404
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500
    
# Definimos las rutas usando el Blueprint
@users_bp.route('/admin/usuaris', methods=['GET'])
@needs_auth
@require_role(required_roles=["admin"])
def list_users(*args, **kwargs):
    try:
        users = orm_list_users()
        user_list = [{'id': u.id_user, 'name': u.username, 'role': u.user_role.name} for u in users]
        return jsonify(user_list)
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

@users_bp.route('/admin/usuaris/<int:id>', methods=['GET'])
@needs_auth
@require_role(required_roles=["admin"])
def get_user_by_id(id,*args, **kwargs):
    try:
        user = orm_get_user_by_id(id)
        if user == None:
            raise UserNotFoundException()
        user_dict = [{'id': user.id_user, 'username': user.username, 'role': user.user_role.name}]
        return jsonify(user_dict)
    except (UserNotFoundException) as e_user_not_found:
        print(e_user_not_found.__str__(),file=sys.stderr)
        print(e_user_not_found.__repr__(),file=sys.stderr)
        return jsonify({'message':'Usuario no encontrado!'}),404
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

@users_bp.route('/admin/usuaris/name/<string:username>', methods=['GET'])
@needs_auth
@require_role(required_roles=["admin"])
def get_user_by_username(username,*args, **kwargs):
    try:
        user : User = orm_get_user_by_username(username)
        if user == None:
            raise UserNotFoundException()
        user_dict = [{'id_user': user.id_user, 'username': user.username, 
            'user_role':{
                'id_user_role':user.user_role.id_user_role,
                'name':user.user_role.name,
            }
          }]
        return jsonify(user_dict)
    except (UserNotFoundException) as e_user_not_found:
        print(e_user_not_found.__str__(),file=sys.stderr)
        print(e_user_not_found.__repr__(),file=sys.stderr)
        return jsonify({'message':'Usuario no encontrado!'}),404
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

# ... (Añadir aquí las rutas POST, PUT, DELETE para usuarios)