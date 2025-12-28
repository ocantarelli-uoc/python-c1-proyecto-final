class MedicalCentre(db.Model):
    __tablename__ = 'medical_centres'
    id_medical_centre = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    id_address = db.Column(db.Integer, db.ForeignKey('addresses.id_address'), nullable=False)
    def __repr__(self):
        return f"<MedicalCentre {self.name}>"