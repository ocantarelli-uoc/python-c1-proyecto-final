import sys
from flask import request
import requests
from dtos.Patient import Patient
from dtos.User import User
from dtos.UserRole import UserRole

def get_patient_by_id(id:int) -> Patient:
    print(id,file=sys.stderr)
    req = requests.Request('GET', 'http://auth_and_admin_bp:5001/api/v1/admin/pacients/'+id)
    r = req.prepare()
    r.headers['Authorization'] = request.headers.get('Authorization')
    r.headers['Content-Type'] = 'application/json'   
    s = requests.Session()
    rs: requests.Response = s.send(r)
    pacient_dict = rs.json()
    pacient : Patient = Patient(id_doctor=pacient_dict['id_doctor'],
        name=pacient_dict['name'],
        user=User(
           id_user=pacient_dict['user']['id_user'],
           username=pacient_dict['user']['username'],
           user_role=UserRole(
           id_user_role=pacient_dict['user']['user_role']['id_user_role'],
              name=pacient_dict['user']['user_role']['name']
           )
        ),
        telephone=pacient_dict['telephone'],
        is_active=pacient_dict['is_active']
    )
    return pacient