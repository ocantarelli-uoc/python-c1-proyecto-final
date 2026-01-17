from models.Address import Address

#It defines the method for getting address by id
def get_address_by_id(id):
    #It gets the address from database through ORM
    address = Address.query.get(id)
    #It returns the gotten address
    return address