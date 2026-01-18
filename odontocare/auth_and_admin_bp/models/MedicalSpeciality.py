from extensions import db
#It defines Model for representation of a medical speciality
class MedicalSpeciality(db.Model):
    __tablename__ = 'medical_specialities'
    id_medical_speciality = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False,unique=True)

    def __repr__(self):
        return f"<MedicalSpeciality {self.name}>"