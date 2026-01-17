from models.UserRole import UserRole
from extensions import db
#It defines the method for creating a user role
def create_user_role(user_role_dict) -> UserRole:
    try:
        #It instances the UserRole class for later adding user role to database through ORM
        created_user_role = UserRole(name=user_role_dict["role_name"])
        #It adds the user role to database through ORM
        db.session.add(created_user_role)
        #It commit the changes
        db.session.commit()
    #It captures the generic exception
    except Exception as e:
        #It rollback the changes
        db.session.rollback()
        #It raise the generic exception above to the method which invoked this
        raise e
    #It returns the created user role
    return created_user_role