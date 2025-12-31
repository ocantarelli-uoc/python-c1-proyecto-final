from flask import Blueprint, jsonify, request
from admin_bp.users.services.get_user_by_id import get_user_by_id
from admin_bp.users.services.create_user import create_user
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role

# Creamos una instancia de Blueprint
# 'users_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
users_bp = Blueprint('users_bp', __name__)

# Definimos las rutas usando el Blueprint
@users_bp.route('/admin/usuaris', methods=['POST'])
@needs_auth
@require_role(required_roles=["admin"])
def add_user(*args, **kwargs):
    try:
        datos = request.get_json()
        createdUser = create_user({
            'username':datos['username'],
            'password':datos['password'],
            'user_role':datos['user_role']
        },user_role_str=None)
        user = get_user_by_id(createdUser.id_user)
        return jsonify({'id': user.id_user, 'username': user.username})
    except Exception as e:
        return jsonify({'message':'Ha ocurrido algún error!'}),500

# ... (Añadir aquí las rutas POST, PUT, DELETE para usuarios)