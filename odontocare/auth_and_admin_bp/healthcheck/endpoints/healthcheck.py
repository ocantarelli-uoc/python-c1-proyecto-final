from flask import Blueprint, jsonify, request

# Creamos una instancia de Blueprint
# "healtcheck_bp" es el nombre del Blueprint
# El segundo parámetro es el nombre del módulo
healthcheck_bp = Blueprint("healthcheck_bp", __name__)

# Definimos las rutas usando el Blueprint
@healthcheck_bp.route("/health", methods=["GET"])
def healthcheck():
    return jsonify({"healtcheck": "OK"}),200