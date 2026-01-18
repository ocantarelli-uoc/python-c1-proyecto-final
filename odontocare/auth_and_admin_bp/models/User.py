from extensions import db
#It defines Model for representation of a user
class User(db.Model):
    __tablename__ = 'users'
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255),unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    id_user_role = db.Column(db.Integer, db.ForeignKey('user_roles.id_user_role'),nullable=False)
    user_role = db.relationship('UserRole')
    def __repr__(self):
        return f"<User {self.username}>"