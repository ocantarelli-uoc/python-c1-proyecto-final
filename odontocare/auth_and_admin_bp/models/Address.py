class Address():
    __tablename__ = 'addresses'
    id_address
    street = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Address {self.street}>"