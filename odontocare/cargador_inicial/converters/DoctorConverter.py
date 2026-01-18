from dtos.UserRole import UserRole
from converters.Converter import Converter
from dtos.Doctor import Doctor
from dtos.User import User
from dtos.MedicalSpeciality import MedicalSpeciality


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
                            user_role=UserRole(
                                id_user_role=None,
                                name=None
                            )
                          ),
                          name=row.name,
                          medical_speciality=MedicalSpeciality(
                              id_medical_speciality=None,
                              name=row.medical_speciality
                          ))
              doctors.append(doctor)
        return doctors