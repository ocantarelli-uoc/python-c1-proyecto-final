from converters.Converter import Converter
from models.MedicalAppointmentStatus import MedicalAppointmentStatus


class MedicalAppointmentStatusConverter(Converter):
  #method that its responsibility it's to convert a dataframe of medical appointment statuses to list of MedicalAppointmentStatus class objects (instances)
     def convert(self,dataFrame) -> list:
        medical_appointment_statuses = []
        for row in dataFrame.itertuples():
            if row.entity_type == "medical_appointment_status":
                medical_appointment_status = MedicalAppointmentStatus(
                    id_medical_status=None,
                    name=row.name,
                )
                medical_appointment_statuses.append(medical_appointment_status)
        return medical_appointment_statuses