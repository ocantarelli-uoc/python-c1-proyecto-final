from flask import request
import requests
from models.Token import Token
from models.Patient import Patient
from models.UserRole import UserRole
from models.User import User

def create_patient(patient:Patient,token:Token) -> Patient:
        body_payload:dict={
            "username":patient.user.username,
            "password":patient.user.password,
            "name":patient.name,
            "telephone":patient.telephone,
        }
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/pacients',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = "Bearer " + token.token
        r.headers['Content-Type'] = 'application/json'
        s = requests.Session()
        rs: requests.Response = s.send(r)
        patient_list = rs.json()
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
        return patient