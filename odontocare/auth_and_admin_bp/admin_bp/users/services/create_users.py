from flask import request
from models.UserRole import UserRole
from models.User import User
from extensions import db

def create_user():
    datos = request.get_json()
    userRole:UserRole = UserRole.query.filter_by(name=datos["user_role"]).first()
    user = User(username=datos["username"],password=datos["password"],id_role=userRole.id_user_role)
    db.session.add(user)
    db.session.commit()
    return user