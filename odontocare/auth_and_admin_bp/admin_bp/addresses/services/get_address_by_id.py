from models.Address import Address

def get_address_by_id(id):
    address = Address.query.get(id)
    return address