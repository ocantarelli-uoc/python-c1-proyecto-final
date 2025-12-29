from models.UserRole import UserRole
from models.User import User
from extensions import db

def get_user_by_id(id):
    user = User.query.get_or_404(id)
    return user