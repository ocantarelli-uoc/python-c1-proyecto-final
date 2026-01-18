from flask import request
import requests
from models.Token import Token
from dtos.MedicalSpeciality import MedicalSpeciality
#It defines a method for creating a request that creates a medical speciality on the auth_and_admin microservice
def create_medical_speciality(medical_speciality:MedicalSpeciality,token:Token) -> MedicalSpeciality:
        #It prepares the body payload for the POST request for creating the medical speciality
        body_payload:dict={
            "medical_speciality_name":medical_speciality.name,
        }
        #It defines the request method (POST) and the URL to be called together with the body specified with Content-Type application/json (json)
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/especialitats_mediques',json=body_payload)
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
        medical_speciality_list = rs.json()
        #If all has gone well, the response has returned a medical speciality body in application/json (json) format
        #and it creates an MedicalSpeciality instance with the recovered data
        medical_speciality : MedicalSpeciality = MedicalSpeciality(
            id_medical_speciality=medical_speciality_list['id_medical_speciality'],
            name=medical_speciality_list['name'],
        )
        #It returns the created medical speciality
        return medical_speciality