import sys
from flask import request
import requests
from dtos.Doctor import Doctor
from dtos.User import User
from dtos.UserRole import UserRole
from dtos.MedicalSpeciality import MedicalSpeciality

def get_doctor_by_id(id:int) -> Doctor:
    print(id,file=sys.stderr)
    req = requests.Request('GET', 'http://auth_and_admin_bp:5001/api/v1/admin/doctors/'+str(id))
    r = req.prepare()
    r.headers['Authorization'] = request.headers.get('Authorization')
    r.headers['Content-Type'] = 'application/json'   
    s = requests.Session()
    rs: requests.Response = s.send(r)
    doctor_rs_list = rs.json()
    #print(doctor_rs_list[0],file=sys.stderr)
    #print(doctor_rs_list[0]['id_doctor'],file=sys.stderr)
    doctor : Doctor = Doctor(
        id_doctor=doctor_rs_list[0]['id_doctor'],
        name=doctor_rs_list[0]['name'],
        medical_speciality=MedicalSpeciality(
            id_medical_speciality=doctor_rs_list[0]['medical_speciality']['id_medical_speciality'],
            name=doctor_rs_list[0]['medical_speciality']['name']
        ),
        user=User(
            id_user=doctor_rs_list[0]['user']['id_user'],
            username=doctor_rs_list[0]['user']['username'],
            user_role=UserRole(
               id_user_role=doctor_rs_list[0]['user']['user_role']['id_user_role'],
               name=doctor_rs_list[0]['user']['user_role']['name']
            )
        )
    )
    return doctor