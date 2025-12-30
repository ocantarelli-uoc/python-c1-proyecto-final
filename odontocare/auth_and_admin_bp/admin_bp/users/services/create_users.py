from flask import request
from models.UserRole import UserRole
from models.User import User
from extensions import db

def create_user(user_role_str):
    datos = request.get_json()
    if user_role_str == None:
        user_role_str = datos["user_role"]
    user_role:UserRole = UserRole.query.filter_by(name=user_role_str).first()
    user = User(username=datos["username"],password=datos["password"],user_role=user_role)
    db.session.add(user)
    db.session.commit()
    return user