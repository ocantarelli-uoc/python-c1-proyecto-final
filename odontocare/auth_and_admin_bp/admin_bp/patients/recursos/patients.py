from flask import Blueprint, jsonify, request

# Creamos una instancia de Blueprint
# 'patients_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
patients_bp = Blueprint('patients_bp', __name__)

# Definimos las rutas usando el Blueprint
@patients_bp.route('/admin/pacients', methods=['POST'])
def add_patient():
    pass

# ... (Añadir aquí las rutas POST, PUT, DELETE para pacientes)