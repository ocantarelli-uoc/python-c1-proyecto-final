from models.UserRole import UserRole
from models.User import User
from extensions import db
from auth_bp.services.hash_password import hash_password
#It defines the method for creating a user
def create_user(user_data,user_role_str):
    try:
        #It checks if user_role_str (provided user role name) it's None for getting role from user_data dictionary
        if user_role_str is None:
            user_role_str = user_data["user_role"]
        #It instances the UserRole class for later adding user to database through ORM
        user_role:UserRole = UserRole.query.filter_by(name=user_role_str).first()
        #It hashes the user password
        hashed_password = hash_password(user_data["password"])
         #It instances the User class for later adding user to database through ORM
        user = User(username=user_data["username"],password=hashed_password,user_role=user_role)
        #It adds the user to database through ORM
        db.session.add(user)
        #It commit the changes
        db.session.commit()
    #It captures the generic exception
    except Exception as e:
        #It rollback the changes
        db.session.rollback()
        #It raise the generic exception above to the method which invoked this
        raise e
    #It returns the created user
    return user