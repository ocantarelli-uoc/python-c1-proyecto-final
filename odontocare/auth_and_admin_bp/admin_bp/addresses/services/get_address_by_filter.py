from models.Address import Address

def get_address_by_filter(street,city):
    address = Address.query.filter_by(street=street,city=city).first()
    return address