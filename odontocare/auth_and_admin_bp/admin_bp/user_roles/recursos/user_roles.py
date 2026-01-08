from flask import Blueprint, jsonify, request
import sys
from admin_bp.user_roles.services.create_user_role import create_user_role
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role
from admin_bp.exceptions.already_exists.UserRoleAlreadyExistsException import UserRoleAlreadyExistsException
from models.UserRole import UserRole
from admin_bp.user_roles.services.get_user_role_by_name import get_user_role_by_name
from admin_bp.user_roles.services.get_user_role_by_id import get_user_role_by_id as orm_get_user_role_by_id
from admin_bp.user_roles.services.list_user_roles import list_user_roles as orm_list_user_roles
from admin_bp.exceptions.not_found.UserRoleNotFoundException import UserRoleNotFoundException
# Creamos una instancia de Blueprint
# 'users_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
users_roles_bp = Blueprint('users_roles_bp', __name__)

# Definimos las rutas usando el Blueprint
@users_roles_bp.route('/admin/rols_usuaris', methods=['POST'])
@needs_auth
@require_role(required_roles=["admin"])
def add_user_role(*args, **kwargs):
    datos = request.get_json()
    try:
        existing_user_role:UserRole = get_user_role_by_name(datos['role_name'])
        if existing_user_role != None:
            raise UserRoleAlreadyExistsException()
        user_role_dict = {
            'role_name':datos['role_name']
        }
        created_user_role = create_user_role(user_role_dict)
        print("abans retornar rol creat",file=sys.stderr)
        print(created_user_role.__str__(),file=sys.stderr)
        print(created_user_role.__repr__(),file=sys.stderr)
        return jsonify({'id': created_user_role.id_user_role, 'name': created_user_role.name})
    except UserRoleAlreadyExistsException as e_user_role_already_exists:
        print(e_user_role_already_exists.__str__(),file=sys.stderr)
        print(e_user_role_already_exists.__repr__(),file=sys.stderr)
        return jsonify({'message':'Rol de Usuario '+datos['role_name']+' ya existe.'}),409
    except UserRoleAlreadyExistsException as e_user_role_not_found:
        print(e_user_role_not_found.__str__(),file=sys.stderr)
        print(e_user_role_not_found.__repr__(),file=sys.stderr)
        return jsonify({'message':'Rol de Usuario '+datos['role_name']+' creado no encontrado.'}),404
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

@users_roles_bp.route('/admin/rols_usuaris', methods=['GET'])
@needs_auth
@require_role(required_roles=["admin"])
def list_user_roles(*args, **kwargs):
    try:
        user_roles = orm_list_user_roles()
        user_roles_list = [{'id': u_r.id_user_role, 'name': u_r.name} for u_r in user_roles]
        return jsonify(user_roles_list)
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

@users_roles_bp.route('/admin/rols_usuaris/<int:id>', methods=['GET'])
@needs_auth
@require_role(required_roles=["admin"])
def get_user_role_by_id(id,*args, **kwargs):
    try:
        user_role : UserRole = orm_get_user_role_by_id(id)
        if user_role is None:
            raise UserRoleNotFoundException()
        user_role_dict = [{'id': user_role.id_user_role, 'name': user_role.name}]
        return jsonify(user_role_dict)
    except (UserRoleNotFoundException) as e_user_not_found:
        print(e_user_not_found.__str__(),file=sys.stderr)
        print(e_user_not_found.__repr__(),file=sys.stderr)
        return jsonify({'message':'Rol de Usuario no encontrado!'}),404
    except (TypeError, ValueError, Exception) as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        return jsonify({'message':'Ha ocurrido algún error!'}),500

# ... (Añadir aquí las rutas POST, PUT, DELETE para usuarios)