from models.User import User

#It defines the method for getting user by id
def get_user_by_id(id):
    #It gets the user from database through ORM
    user = User.query.get(id)
    #It returns the gotten user
    return user