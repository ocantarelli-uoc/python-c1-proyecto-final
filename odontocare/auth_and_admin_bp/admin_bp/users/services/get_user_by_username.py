from models.User import User

#It defines the method for getting user by username
def get_user_by_username(username):
    #It gets the user from database through ORM
    user = User.query.filter_by(username=username).first()
    #It returns the gotten user
    return user