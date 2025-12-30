from flask import Blueprint, jsonify, request
from admin_bp.users.services.create_users import create_user
from admin_bp.patients.services.create_patient import create_patient

# Creamos una instancia de Blueprint
# 'patients_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
patients_bp = Blueprint('patients_bp', __name__)

# Definimos las rutas usando el Blueprint
@patients_bp.route('/admin/pacients', methods=['POST'])
def add_patient():
    created_user = create_user(user_role_str="patient")
    created_patient = create_patient(created_user)
    return jsonify({'id': created_patient.id_patient, 'name': created_patient.name})

# ... (Añadir aquí las rutas POST, PUT, DELETE para pacientes)