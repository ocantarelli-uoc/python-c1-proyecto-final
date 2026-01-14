from converters.Converter import Converter
from models.Address import Address


class AddressConverter(Converter):
  #method that its responsibility it's to convert a dataframe of addresses to list of Address class objects (instances)
     def convert(self,dataFrame) -> list:
        addresses = []
        for row in dataFrame.itertuples():
            if row.entity_type == "address":
                address = Address(
                    id_address=None,
                    street=row.street,
                    city=row.city,
                )
                addresses.append(address)
        return addresses