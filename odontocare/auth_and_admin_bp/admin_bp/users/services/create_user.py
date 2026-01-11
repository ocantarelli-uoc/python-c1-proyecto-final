from models.UserRole import UserRole
from models.User import User
from extensions import db
from auth_bp.services.hash_password import hash_password

def create_user(user_data,user_role_str):
    #datos = request.get_json()
    try:
        if user_role_str is None:
            user_role_str = user_data["user_role"]
        user_role:UserRole = UserRole.query.filter_by(name=user_role_str).first()
        hashed_password = hash_password(user_data["password"])
        user = User(username=user_data["username"],password=hashed_password,user_role=user_role)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    return user