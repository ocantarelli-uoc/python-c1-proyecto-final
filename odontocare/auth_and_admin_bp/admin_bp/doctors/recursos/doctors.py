from flask import Blueprint, jsonify, request
from admin_bp.users.services.create_user import create_user
from admin_bp.doctors.services.create_doctor import create_doctor
from decorators.needs_authorization import needs_auth
from decorators.require_role import require_role

# Creamos una instancia de Blueprint
# 'doctors_bp' es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
doctors_bp = Blueprint('doctors_bp', __name__)

# Definimos las rutas usando el Blueprint
@doctors_bp.route('/admin/doctors', methods=['POST'])
@needs_auth
@require_role(required_roles=["admin"])
def add_doctor(*args, **kwargs):
    datos = request.get_json()
    created_user = create_user({
        'username':datos['username'],
        'password':datos['password']
    },user_role_str="doctor")
    created_doctor = create_doctor(created_user)
    return jsonify({'id': created_doctor.id_doctor, 'name': created_doctor.name})

# ... (Añadir aquí las rutas POST, PUT, DELETE para médicos)