from sqlalchemy import select
from extensions import db
from models.UserRole import UserRole
#It defines the method for listing user roles
def list_user_roles() -> list[UserRole]:
    #It declares the variable for adding the user roles gotten
    #from database through ORM
    user_roles : list[UserRole] = []
    #It selects the user roles from database through ORM
    stmt = select(UserRole)
    #for every user role gotten from database
    for row in db.session.execute(stmt):
         #It adds the current user role to the list
        user_roles.append(row.UserRole)
    #It returns the user role list gotten from database
    #through ORM
    return user_roles