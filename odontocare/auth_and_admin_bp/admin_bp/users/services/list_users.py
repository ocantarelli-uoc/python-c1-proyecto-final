from sqlalchemy import select
from extensions import db
from models.User import User
#It defines the method for listing user
def list_users() -> list[User]:
    #It declares the variable for adding the user gotten
    #from database through ORM
    users : list[User] = []
    #It selects the user from database through ORM
    stmt = select(User)
    #for every user gotten from database
    for row in db.session.execute(stmt):
         #It adds the current user to the list
        users.append(row.User)
    #It returns the user list gotten from database
    #through ORM
    return users