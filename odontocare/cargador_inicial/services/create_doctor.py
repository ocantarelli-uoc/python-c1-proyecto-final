from flask import request
import requests
from models.Token import Token
from models.Doctor import Doctor
from models.UserRole import UserRole
from models.User import User
from models.MedicalSpeciality import MedicalSpeciality

def create_doctor(doctor:Doctor,token:Token) -> Doctor:
        body_payload:dict={
            "username":doctor.user.username,
            "password":doctor.user.password,
            "name":doctor.name,
            "medical_speciality":doctor.medical_speciality.name,
        }
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/doctors',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = "Bearer " + token.token
        r.headers['Content-Type'] = 'application/json'
        s = requests.Session()
        rs: requests.Response = s.send(r)
        doctors_list = rs.json()
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
        return doctor