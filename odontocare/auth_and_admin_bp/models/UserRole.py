from extensions import db
#It defines Model for representation of a user role
class UserRole(db.Model):
    __tablename__ = 'user_roles'
    id_user_role = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False,unique=True)

    def __repr__(self):
        return f"<UserRole {self.name}>"