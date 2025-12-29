from extensions import db
class Doctor(db.Model):
    __tablename__ = 'doctors'
    id_patient = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id_user'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    id_medical_speciality = db.Column(db.Integer, db.ForeignKey('medical_specialities.id_medical_speciality'), nullable=False)
    def __repr__(self):
        return f"<Doctor {self.name}>"