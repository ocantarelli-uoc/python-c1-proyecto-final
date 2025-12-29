from extensions import db
class User(db.Model):
    __tablename__ = 'users'
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    id_role = db.Column(db.Integer, db.ForeignKey('user_roles.id_user_role'), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"