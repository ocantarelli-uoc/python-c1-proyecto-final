from flask import request
from models.UserRole import UserRole
from extensions import db

def create_user_role(user_role_dict):
    created_user_role = UserRole(name=user_role_dict["role_name"])
    db.session.add(created_user_role)
    db.session.commit()
    return created_user_role