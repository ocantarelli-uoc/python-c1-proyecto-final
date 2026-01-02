from sqlalchemy import select
from sqlalchemy.orm import Session
from models.UserRole import UserRole
def list_user_roles() -> list[UserRole]:
    user_roles : list[UserRole] = []
    stmt = select(UserRole)
    for row in Session.execute(stmt):
        user_roles.append(row.UserRole)
    return user_roles