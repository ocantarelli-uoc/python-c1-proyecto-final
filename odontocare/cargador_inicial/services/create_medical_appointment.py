from flask import request
import json
import requests
from models.Token import Token
from models.MedicalAppointment import MedicalAppointment
from models.MedicalAppointmentStatus import MedicalAppointmentStatus
#It defines a method for creating a request that creates a medical appointment on the cites microservice
def create_medical_appointment(medical_appointment:MedicalAppointment,token:Token) -> MedicalAppointment:
        #It prepares the body payload for the POST request for creating the medical appointment
        body_payload:dict={
            "appointment_date":str(medical_appointment.appointment_date),
            "id_doctor":medical_appointment.id_doctor,
            "id_patient":medical_appointment.id_patient,
            "id_medical_center":medical_appointment.id_medical_center,
            "motiu":medical_appointment.motiu,
            "id_action_user":medical_appointment.id_action_user,
        }
        #It defines the request method (POST) and the URL to be called together with the body specified with Content-Type application/json (json)
        req = requests.Request('POST','http://cites_bp:5002/api/v1/cites',json=body_payload)
        #It prepares the request with the previous defined configuration
        r = req.prepare()
        #It defines the authorization header (Authorization), specifiying it's of the type Bearer Token, together with the user token
        r.headers['Authorization'] = "Bearer " + token.token
        #It defines the header Content-Type, specifying that the content provided on the body it's of the type application/json (json)
        r.headers['Content-Type'] = 'application/json'
        #It defines the header Accept, which specifies that the client accepts specifically content as response of the type application/json (json)
        r.headers['Accept'] = 'application/json'
        #It starts the request session
        s = requests.Session()
        #It sends the request through the request session, and it gets the response (valid or not)
        rs: requests.Response = s.send(r)
        #If the response returns, it tries to parse it in application/json
        medical_appointment_response_obj = rs.json()
        #print("Medical Appointment JSON")
        print(json.dumps(medical_appointment_response_obj))
        #If all has gone well, the response has returned a medical appointment body in application/json (json) format
        #and it creates an MedMedicalAppointmenticalAppointmentStatus instance with the recovered data
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
        #It returns the created medical appointment
        return medical_appointment