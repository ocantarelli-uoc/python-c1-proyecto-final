from cargador_inicial.converters.Converter import Converter
from cargador_inicial.dtos.Patient import Patient
from cargador_inicial.dtos.User import User


class PatientConverter(Converter):
  #method that its responsibility it's to convert a dataframe of patients to list of Patient class objects (instances)
     def convert(self,dataFrame) -> list:
        patients = []
        for row in dataFrame.itertuples():
            if row.entity_type == "patient":
              patient = Patient(id_patient=None,
                          user=User(
                            id_user=None,
                            username=row.username,
                            password=row.password,
                            user_role=None
                          ),
                          name=row.name,
                          telephone=row.telephone,
                          is_active=row.is_active)
              patients.append(patient)
        return patients