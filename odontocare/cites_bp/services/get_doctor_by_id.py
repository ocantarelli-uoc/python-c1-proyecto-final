import sys
from flask import request
import requests
from dtos.Doctor import Doctor

def get_doctor_by_id(id:int) -> Doctor:
    print(id,file=sys.stderr)
    req = requests.Request('GET', 'http://auth_and_admin_bp:5001/api/v1/admin/doctors/'+id)
    r = req.prepare()
    r.headers['Authorization'] = request.headers.get('Authorization')
    r.headers['Content-Type'] = 'application/json'   
    s = requests.Session()
    rs: requests.Response = s.send(r)
    doctor_dict = rs.json()
    #doctor : Doctor = Doctor(id_patient=)
    return doctor