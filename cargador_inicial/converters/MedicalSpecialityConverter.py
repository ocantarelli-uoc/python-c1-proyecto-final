from cargador_inicial.converters.Converter import Converter
from cargador_inicial.dtos.MedicalSpeciality import MedicalSpeciality


class MedicalSpecialityConverter(Converter):
  #method that its responsibility it's to convert a dataframe of medical_specialities to list of MedicalSpeciality class objects (instances)
     def convert(self,dataFrame) -> list:
        medical_specialities = []
        for row in dataFrame.itertuples():
            medical_speciality = MedicalSpeciality(
                id_medical_speciality=None,
                name=row.name,
            )
            medical_specialities.append(medical_speciality)
        return medical_specialities