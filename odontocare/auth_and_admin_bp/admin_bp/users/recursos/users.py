from flask import Blueprint, jsonify, request

# Creamos una instancia de Blueprint
# 'users_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
users_bp = Blueprint('users_bp', __name__)

# Definimos las rutas usando el Blueprint
@users_bp.route('/admin/usuaris', methods=['POST'])
def add_user():
    pass

# ... (Añadir aquí las rutas POST, PUT, DELETE para usuarios)