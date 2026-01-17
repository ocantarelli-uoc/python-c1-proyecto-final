from models.UserRole import UserRole

#It defines the method for getting user role by id
def get_user_role_by_id(id) -> UserRole:
    #It gets the user role from database through ORM
    user_role : UserRole = UserRole.query.get(id)
    #It returns the gotten user role
    return user_role