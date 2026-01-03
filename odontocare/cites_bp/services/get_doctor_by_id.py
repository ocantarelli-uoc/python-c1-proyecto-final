import sys
from flask import request
import requests
from dtos.Doctor import Doctor
from dtos.User import User
from dtos.UserRole import UserRole
from dtos.MedicalSpeciality import MedicalSpeciality

def get_doctor_by_id(id:int) -> Doctor:
    print(id,file=sys.stderr)
    req = requests.Request('GET', 'http://auth_and_admin_bp:5001/api/v1/admin/doctors/'+id)
    r = req.prepare()
    r.headers['Authorization'] = request.headers.get('Authorization')
    r.headers['Content-Type'] = 'application/json'   
    s = requests.Session()
    rs: requests.Response = s.send(r)
    doctor_dict = rs.json()
    doctor : Doctor = Doctor(
        id_doctor=doctor_dict['id_doctor'],
        name=doctor_dict['name'],
        medical_speciality=MedicalSpeciality(
            id_medical_speciality=doctor_dict['medical_speciality']['id_medical_speciality'],
            name=doctor_dict['medical_speciality']['name']
        ),
        user=User(
            id_user=doctor_dict['user']['id_user'],
            username=doctor_dict['user']['username'],
            user_role=UserRole(
               id_user_role=doctor_dict['user']['user_role']['id_user_role'],
               name=doctor_dict['user']['user_role']['name']
            )
        )
    )
    return doctor