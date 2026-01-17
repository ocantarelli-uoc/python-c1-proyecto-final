from flask import request
import requests
from models.Token import Token
from models.MedicalAppointmentStatus import MedicalAppointmentStatus

def create_medical_appointment_status(medical_appointment_status:MedicalAppointmentStatus,token:Token) -> MedicalAppointmentStatus:
        body_payload:dict={
            "status_name":medical_appointment_status.name,
        }
        req = requests.Request('POST','http://cites_bp:5002/api/v1/estats_cites',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = "Bearer " + token.token
        r.headers['Content-Type'] = 'application/json'
        s = requests.Session()
        rs: requests.Response = s.send(r)
        medical_appointment_status_list = rs.json()
        medical_appointment_status : MedicalAppointmentStatus = MedicalAppointmentStatus(
            id_medical_status=medical_appointment_status_list['id_medical_status'],
            name=medical_appointment_status_list['name'],
        )
        return medical_appointment_status