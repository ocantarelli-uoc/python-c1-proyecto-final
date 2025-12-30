from extensions import db
class Address(db.Model):
    __tablename__ = 'addresses'
    id_address = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Address {self.street}>"