from flask import request
from models.UserRole import UserRole
from models.User import User
from extensions import db

def create_user(user_role):
    datos = request.get_json()
    if user_role == None:
        user_role = datos["user_role"]
    userRole:UserRole = UserRole.query.filter_by(name=user_role).first()
    user = User(username=datos["username"],password=datos["password"],id_role=userRole.id_user_role)
    db.session.add(user)
    db.session.commit()
    return user