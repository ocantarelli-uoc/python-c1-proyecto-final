from flask import Blueprint, jsonify, request
from admin_bp.users.services.get_user_by_id import get_user_by_id
from admin_bp.users.services.create_users import create_user

# Creamos una instancia de Blueprint
# 'users_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
users_bp = Blueprint('users_bp', __name__)

# Definimos las rutas usando el Blueprint
@users_bp.route('/admin/usuaris', methods=['POST'])
def add_user():
    createdUser = create_user(user_role=None)
    user = get_user_by_id(createdUser.id_user)
    return jsonify({'id': user.id_user, 'username': user.username})

# ... (Añadir aquí las rutas POST, PUT, DELETE para usuarios)