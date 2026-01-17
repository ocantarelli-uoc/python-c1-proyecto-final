from models.Address import Address

#It defines the method for getting address by filter (city and street)
def get_address_by_filter(street,city):
    #It gets the address from database through ORM
    address = Address.query.filter_by(street=street,city=city).first()
    #It returns the gotten address
    return address