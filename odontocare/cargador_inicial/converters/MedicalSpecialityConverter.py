from converters.Converter import Converter
from models.MedicalSpeciality import MedicalSpeciality


class MedicalSpecialityConverter(Converter):
  #method that its responsibility it's to convert a dataframe of medical_specialities to list of MedicalSpeciality class objects (instances)
     def convert(self,dataFrame) -> list:
        medical_specialities = []
        for row in dataFrame.itertuples():
            if row.entity_type == "medical_speciality":
                medical_speciality = MedicalSpeciality(
                    id_medical_speciality=None,
                    name=row.name,
                )
                medical_specialities.append(medical_speciality)
        return medical_specialities