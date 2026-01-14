from converters.Converter import Converter
from models.MedicalCenter import MedicalCenter
from models.Address import Address

class MedicalCenterConverter(Converter):
  #method that its responsibility it's to convert a dataframe of medical_centers to list of MedicalCenter class objects (instances)
     def convert(self,dataFrame) -> list:
        medical_centers = []
        for row in dataFrame.itertuples():
            if row.entity_type == "medical_center":
                medical_center = MedicalCenter(
                    id_medical_center=None,
                    address=Address(
                        id_address=row.id_address,
                        street=None,
                        city=None,
                    ),
                    name=row.name,
                )
                medical_centers.append(medical_center)
        return medical_centers