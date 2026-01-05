import sys
from flask import request
import requests
from dtos.Patient import Patient
from dtos.User import User
from dtos.UserRole import UserRole

def get_patient_by_id(id:int) -> Patient:
    print(id,file=sys.stderr)
    req = requests.Request('GET', 'http://auth_and_admin_bp:5001/api/v1/admin/pacients/'+str(id))
    r = req.prepare()
    r.headers['Authorization'] = request.headers.get('Authorization')
    r.headers['Content-Type'] = 'application/json'   
    s = requests.Session()
    rs: requests.Response = s.send(r)
    patient_rs_list = rs.json()
    patient = None
    if patient_rs_list is not None and isinstance(patient_rs_list,list) and len(patient_rs_list) >= 1:
      patient : Patient = Patient(id_patient=patient_rs_list[0]['id_patient'],
         name=patient_rs_list[0]['name'],
         user=User(
            id_user=patient_rs_list[0]['user']['id_user'],
            username=patient_rs_list[0]['user']['username'],
            user_role=UserRole(
            id_user_role=patient_rs_list[0]['user']['user_role']['id_user_role'],
               name=patient_rs_list[0]['user']['user_role']['name']
            )
         ),
         telephone=patient_rs_list[0]['telephone'],
         is_active=patient_rs_list[0]['is_active']
      )
    return patient