import sys
from flask import request
import requests
from dtos.Token import Token
from dtos.MedicalAppointmentStatus import MedicalAppointmentStatus
from dtos.MedicalAppointment import MedicalAppointment

def create_medical_appointment(medical_appointment:MedicalAppointment,token:Token) -> MedicalAppointment:
    body_payload:dict={
        "appointment_date":str(medical_appointment.appointment_date),
        "id_doctor":medical_appointment.id_doctor,
        "id_patient":medical_appointment.id_patient,
        "id_medical_center":medical_appointment.id_medical_center,
        "motiu":medical_appointment.motiu,
        "id_action_user":medical_appointment.id_action_user,
    }
    req = requests.post('http://localhost:5002/api/v1/admin/cites',json=body_payload)
    r = req.prepare()
    r.headers['Authorization'] = token.token
    r.headers['Content-Type'] = 'application/json'
    s = requests.Session()
    rs: requests.Response = s.send(r)
    medical_appointment_list = rs.json()
    medical_appointment : MedicalAppointment = MedicalAppointment(
        id_doctor=medical_appointment_list[0]['id_doctor'],
        id_patient=medical_appointment_list[0]['id_patient'],
        id_medical_center=medical_appointment_list[0]['id_medical_center'],
        appointment_date=medical_appointment_list[0]['appointment_date'],
        motiu=medical_appointment_list[0]['motiu'],
        id_action_user=medical_appointment_list[0]['id_action_user'],
    )
    return medical_appointment
