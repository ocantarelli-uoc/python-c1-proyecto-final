from flask import request
import requests
from models.Token import Token
from dtos.Patient import Patient
from dtos.UserRole import UserRole
from dtos.User import User
#It defines a method for creating a request that creates a patient on the auth_and_admin microservice
def create_patient(patient:Patient,token:Token) -> Patient:
        #It prepares the body payload for the POST request for creating the patient
        body_payload:dict={
            "username":patient.user.username,
            "password":patient.user.password,
            "name":patient.name,
            "telephone":patient.telephone,
        }
        #It defines the request method (POST) and the URL to be called together with the body specified with Content-Type application/json (json)
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/pacients',json=body_payload)
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
        patient_list = rs.json()
        #If all has gone well, the response has returned a patient body in application/json (json) format
        #and it creates an Patient instance with the recovered data
        patient : Patient = Patient(
                    id_patient=patient_list['id_patient'],
                    name=patient_list['name'],
                    telephone=patient_list['telephone'],
                    is_active=patient_list['is_active'],
                    user=User(id_user=patient_list['user']['id_user'],
                        username=patient_list['user']['username'],
                        password=None,
                            user_role=UserRole(
                                id_user_role=patient_list['user']['user_role']['id_user_role'],
                                name=patient_list['user']['user_role']['name']
                            )
                    )
                )
        #It returns the created patient
        return patient