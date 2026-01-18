from converters.Converter import Converter
from dtos.MedicalAppointment import MedicalAppointment
from dtos.Doctor import Doctor
from dtos.Patient import Patient
from dtos.User import User 
from dtos.MedicalAppointmentStatus import MedicalAppointmentStatus

class MedicalAppointmentConverter(Converter):
  #method that its responsibility it's to convert a dataframe of medical appointments to list of MedicalAppointment class objects (instances)
     def convert(self,dataFrame) -> list:
        medical_appointments = []
        for row in dataFrame.itertuples():
            if row.entity_type == "medical_appointment":
                medical_appointment = MedicalAppointment(
                    id_medical_appointment=None,
                    appointment_date=row.appointment_date,
                    id_doctor=row.id_doctor,
                    id_patient=row.id_patient,
                    motiu=row.motiu,
                    medical_appointment_status=MedicalAppointmentStatus(
                        id_medical_status=None,
                        name=None,
                    ),
                    id_action_user=row.id_action_user,
                    id_medical_center=row.id_medical_center
                )
                medical_appointments.append(medical_appointment)
        return medical_appointments