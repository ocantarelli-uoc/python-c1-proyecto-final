from cargador_inicial.converters.Converter import Converter
from cargador_inicial.dtos.Doctor import Doctor
from cargador_inicial.dtos.User import User
from cargador_inicial.dtos.MedicalSpeciality import MedicalSpeciality


class DoctorConverter(Converter):
  #method that its responsibility it's to convert a dataframe of doctors to list of Doctor class objects (instances)
     def convert(self,dataFrame) -> list:
        doctors = []
        for row in dataFrame.itertuples():
            if row.entity_type == "doctor":
              doctor = Doctor(id_doctor=None,
                          user=User(
                            id_user=None,
                            username=row.username,
                            password=row.password,
                            user_role=None
                          ),
                          name=row.name,
                          medical_speciality=MedicalSpeciality(
                              id_medical_speciality=None,
                              name=row.medical_speciality
                          ))
              doctors.append(doctor)
        return doctors