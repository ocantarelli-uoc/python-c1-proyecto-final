from flask import Blueprint, jsonify, request

# Creamos una instancia de Blueprint
# 'auth_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
auth_bp = Blueprint('auth_bp', __name__)

# Definimos las rutas usando el Blueprint
@auth_bp.route('/admin/usuaris', methods=['POST'])
def add_usuari():
    pass

# ... (Añadir aquí las rutas POST, PUT, DELETE para citas)