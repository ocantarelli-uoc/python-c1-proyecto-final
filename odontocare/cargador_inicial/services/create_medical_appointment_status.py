from flask import request
import requests
from models.Token import Token
from dtos.MedicalAppointmentStatus import MedicalAppointmentStatus
#It defines a method for creating a request that creates a medical appointment status on the cites microservice
def create_medical_appointment_status(medical_appointment_status:MedicalAppointmentStatus,token:Token) -> MedicalAppointmentStatus:
        #It prepares the body payload for the POST request for creating the medical appointment status
        body_payload:dict={
            "status_name":medical_appointment_status.name,
        }
        #It defines the request method (POST) and the URL to be called together with the body specified with Content-Type application/json (json)
        req = requests.Request('POST','http://cites_bp:5002/api/v1/estats_cites',json=body_payload)
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
        medical_appointment_status_list = rs.json()
        #If all has gone well, the response has returned a medical appointment status body in application/json (json) format
        #and it creates an MedicalAppointmentStatus instance with the recovered data
        medical_appointment_status : MedicalAppointmentStatus = MedicalAppointmentStatus(
            id_medical_status=medical_appointment_status_list['id_medical_status'],
            name=medical_appointment_status_list['name'],
        )
        #It returns the created medical appointment status
        return medical_appointment_status