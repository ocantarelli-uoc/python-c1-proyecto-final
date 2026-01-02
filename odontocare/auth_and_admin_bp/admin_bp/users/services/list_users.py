from sqlalchemy import select
from extensions import db
from models.User import User
def list_users() -> list[User]:
    users : list[User] = []
    stmt = select(User)
    for row in db.session.execute(stmt):
        users.append(row.User)
    return users
    