from models.User import User

def get_user_by_id(id):
    user = User.query.get(id)
    return user