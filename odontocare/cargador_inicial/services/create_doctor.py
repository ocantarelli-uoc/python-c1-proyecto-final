from flask import request
import requests
from models.Token import Token
from dtos.Doctor import Doctor
from dtos.UserRole import UserRole
from dtos.User import User
from dtos.MedicalSpeciality import MedicalSpeciality
#It defines a method for creating a request that creates a doctor on the auth_and_admin microservice
def create_doctor(doctor:Doctor,token:Token) -> Doctor:
        #It prepares the body payload for the POST request for creating the doctor
        body_payload:dict={
            "username":doctor.user.username,
            "password":doctor.user.password,
            "name":doctor.name,
            "medical_speciality":doctor.medical_speciality.name,
        }
        #It defines the request method (POST) and the URL to be called together with the body specified with Content-Type application/json (json)
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/doctors',json=body_payload)
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
        doctors_list = rs.json()
        #If all has gone well, the response has returned a doctor body in application/json (json) format
        #and it creates an Doctor instance with the recovered data
        doctor : Doctor = Doctor(
                    id_doctor=doctors_list['id_doctor'],
                    name=doctors_list['name'],
                    user=User(id_user=doctors_list['user']['id_user'],
                        username=doctors_list['user']['username'],
                        password=None,
                            user_role=UserRole(
                                id_user_role=doctors_list['user']['user_role']['id_user_role'],
                                name=doctors_list['user']['user_role']['name']
                            )
                    ),
                    medical_speciality=MedicalSpeciality(
                                id_medical_speciality=doctors_list['medical_speciality']['id_medical_speciality'],
                                name=doctors_list['medical_speciality']['name']
                            )
                )
        #It returns the created doctor
        return doctor