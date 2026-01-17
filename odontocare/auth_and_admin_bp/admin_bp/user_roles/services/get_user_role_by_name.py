from models.UserRole import UserRole

#It defines the method for getting user role by name
def get_user_role_by_name(role_name):
    #It gets the user role from database through ORM
    user_role = UserRole.query.filter_by(name=role_name).first()
    #It returns the gotten user role
    return user_role