from flask import Blueprint, jsonify, request

# Creamos una instancia de Blueprint
# 'centers_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
centers_bp = Blueprint('centers_bp', __name__)

# Definimos las rutas usando el Blueprint
@centers_bp.route('/admin/centres', methods=['POST'])
def add_center():
    pass

# ... (Añadir aquí las rutas POST, PUT, DELETE para centros)