from flask import Blueprint, jsonify, request

# Creamos una instancia de Blueprint
# 'doctors_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
doctors_bp = Blueprint('doctors_bp', __name__)

# Definimos las rutas usando el Blueprint
@doctors_bp.route('/admin/doctors', methods=['POST'])
def add_doctor():
    pass

# ... (Añadir aquí las rutas POST, PUT, DELETE para médicos)