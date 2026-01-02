from models.UserRole import UserRole

def get_user_role_by_id(id) -> UserRole:
    user_role = UserRole.query.get(id)
    return user_role