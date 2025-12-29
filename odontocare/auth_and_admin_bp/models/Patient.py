from extensions import db
class Patient(db.Model):
    __tablename__ = 'patients'
    id_patient = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id_user'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    telephone = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<Patient {self.name}>"