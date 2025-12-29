from flask import Blueprint, jsonify, request
from admin_bp.user_roles.services.get_user_role_by_id import get_user_role_by_id
from admin_bp.user_roles.services.create_user_role import create_user_role

# Creamos una instancia de Blueprint
# 'users_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
users_roles_bp = Blueprint('users_roles_bp', __name__)

# Definimos las rutas usando el Blueprint
@users_roles_bp.route('/admin/rols_usuaris', methods=['POST'])
def add_user():
    created_user_role = create_user_role()
    user_role = get_user_role_by_id(created_user_role.id_user_role)
    return jsonify({'id': user_role.id_user_role, 'name': user_role.name})

# ... (Añadir aquí las rutas POST, PUT, DELETE para usuarios)