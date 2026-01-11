from models.User import User

def get_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    return user