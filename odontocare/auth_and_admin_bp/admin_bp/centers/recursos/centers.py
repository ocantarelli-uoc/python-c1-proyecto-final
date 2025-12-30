from flask import Blueprint, jsonify, request
from admin_bp.centers.services.create_center import create_center

# Creamos una instancia de Blueprint
# 'centers_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
centers_bp = Blueprint('centers_bp', __name__)

# Definimos las rutas usando el Blueprint
@centers_bp.route('/admin/centres', methods=['POST'])
def add_center():
    created_center = create_center()
    return jsonify({'id': created_center.id_medical_center, 'name': created_center.name})

# ... (Añadir aquí las rutas POST, PUT, DELETE para centros)