from sqlalchemy import select
from sqlalchemy.orm import Session
from models.User import User
def list_users() -> list[User]:
    users : list[User] = []
    stmt = select(User)
    for row in Session.execute(stmt):
        users.append(row.User)
    return users
    