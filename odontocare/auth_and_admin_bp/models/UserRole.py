from extensions import db
class UserRole(db.Model):
    __tablename__ = 'user_roles'
    id_user_role = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<UserRole {self.name}>"