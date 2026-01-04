from extensions import db
class MedicalAppointmentStatus(db.Model):
    __tablename__ = 'medical_appointment_statuses'
    id_medical_status = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<MedicalAppointmentStatus {self.name}>"