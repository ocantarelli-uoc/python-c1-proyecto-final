from models.UserRole import UserRole

def get_user_role_by_name(role_name):
    user_role = UserRole.query.filter_by(name=role_name).first()
    return user_role