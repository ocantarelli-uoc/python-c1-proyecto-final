import sys
from flask import request
import requests
from dtos.Token import Token
from dtos.User import User
from dtos.UserRole import UserRole
from dtos.Doctor import Doctor
from dtos.MedicalSpeciality import MedicalSpeciality

def create_doctor(doctor:Doctor,token:Token) -> Doctor:
    body_payload:dict={
        "username":doctor.user.username,
        "password":doctor.user.password,
        "name":doctor.name,
        "medical_speciality":doctor.medical_speciality.name,
    }
    req = requests.post('http://localhost:5001/api/v1/admin/doctors',json=body_payload)
    r = req.prepare()
    r.headers['Authorization'] = token.token
    r.headers['Content-Type'] = 'application/json'
    s = requests.Session()
    rs: requests.Response = s.send(r)
    doctors_list = rs.json()
    doctor : Doctor = Doctor(
                id_doctor=doctors_list[0]['id_doctor'],
                name=doctors_list[0]['name'],
                user=User(id_user=doctors_list[0]['user']['id_user'],
                      username=doctors_list[0]['user']['username'],
                       password=doctors_list[0]['user']['password'],
                        user_role=UserRole(
                            id_user_role=doctors_list[0]['user']['user_role']['id_user_role'],
                            name=doctors_list[0]['user']['user_role']['name']
                        )
                 ),
                 medical_speciality=MedicalSpeciality(
                            id_medical_speciality=doctors_list[0]['medical_speciality']['id_medical_speciality'],
                            name=doctors_list[0]['medical_speciality']['name']
                        )
              )
    return doctor