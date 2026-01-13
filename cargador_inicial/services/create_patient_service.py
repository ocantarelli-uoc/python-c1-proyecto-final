import sys
from flask import request
import requests
from dtos.Token import Token
from dtos.User import User
from dtos.UserRole import UserRole
from dtos.Patient import Patient

def create_patient(patient:Patient,token:Token) -> Patient:
    body_payload:dict={
        "username":patient.user.username,
        "password":patient.user.password,
        "name":patient.name,
        "telephone":patient.telephone,
    }
    req = requests.post('http://localhost:5001/api/v1/admin/pacients',json=body_payload)
    r = req.prepare()
    r.headers['Authorization'] = token.token
    r.headers['Content-Type'] = 'application/json'
    s = requests.Session()
    rs: requests.Response = s.send(r)
    patient_list = rs.json()
    patient : Patient = Patient(
                id_patient=patient_list[0]['id_patient'],
                name=patient_list[0]['name'],
                telephone=patient_list[0]['telephone'],
                is_active=patient_list[0]['is_active'],
                user=User(id_user=patient_list[0]['user']['id_user'],
                      username=patient_list[0]['user']['username'],
                       password=patient_list[0]['user']['password'],
                        user_role=UserRole(
                            id_user_role=patient_list[0]['user']['user_role']['id_user_role'],
                            name=patient_list[0]['user']['user_role']['name']
                        )
                 )
              )
    return patient