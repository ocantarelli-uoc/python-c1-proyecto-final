from flask import request
import json
import requests
from models.Token import Token
from models.MedicalAppointment import MedicalAppointment
from models.MedicalAppointmentStatus import MedicalAppointmentStatus

def create_medical_appointment(medical_appointment:MedicalAppointment,token:Token) -> MedicalAppointment:
        body_payload:dict={
            "appointment_date":str(medical_appointment.appointment_date),
            "id_doctor":medical_appointment.id_doctor,
            "id_patient":medical_appointment.id_patient,
            "id_medical_center":medical_appointment.id_medical_center,
            "motiu":medical_appointment.motiu,
            "id_action_user":medical_appointment.id_action_user,
        }
        req = requests.Request('POST','http://cites_bp:5002/api/v1/cites',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = "Bearer " + token.token
        r.headers['Content-Type'] = 'application/json'
        s = requests.Session()
        rs: requests.Response = s.send(r)
        medical_appointment_response_obj = rs.json()
        #print("Medical Appointment JSON")
        print(json.dumps(medical_appointment_response_obj))
        medical_appointment : MedicalAppointment = MedicalAppointment(
            id_medical_appointment=medical_appointment_response_obj['id_medical_appointment'],
            medical_appointment_status=MedicalAppointmentStatus(id_medical_status=medical_appointment_response_obj['medical_appointment_status']['id_medical_status'],
                        name=medical_appointment_response_obj['medical_appointment_status']['name']),
            id_doctor=medical_appointment_response_obj['id_doctor'],
            id_patient=medical_appointment_response_obj['id_patient'],
            id_medical_center=medical_appointment_response_obj['id_medical_center'],
            appointment_date=medical_appointment_response_obj['appointment_date'],
            motiu=medical_appointment_response_obj['motiu'],
            id_action_user=medical_appointment_response_obj['id_action_user'],
        )
        return medical_appointment