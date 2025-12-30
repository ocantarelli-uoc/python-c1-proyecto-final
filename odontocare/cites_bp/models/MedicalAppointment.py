class MedicalAppointment(db.Model):
    __tablename__ = 'medical_appointments'
    id_appointment = db.Column(db.Integer, primary_key=True)
    appointment_date = db.Column(db.Date, nullable=False)
    motiu = db.Column(db.String(255), nullable=False)
    medical_appointment_status = db.relationship('MedicalAppointmentStatus')
    id_doctor = db.Column(db.Integer, nullable=False)
    id_medical_centre = db.Column(db.Integer, nullable=False)
    id_patient = db.Column(db.Integer, nullable=False)
    id_action_user = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f"<MedicalCenter {self.name}>"