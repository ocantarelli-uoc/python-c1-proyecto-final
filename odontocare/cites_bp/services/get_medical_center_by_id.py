import sys
from flask import request
import requests
from dtos.MedicalCenter import MedicalCenter
from dtos.Address import Address

def get_medical_center_by_id(id:int) -> MedicalCenter:
    print(id,file=sys.stderr)
    req = requests.Request('GET', 'http://auth_and_admin_bp:5001/api/v1/admin/centres/'+id)
    r = req.prepare()
    r.headers['Authorization'] = request.headers.get('Authorization')
    r.headers['Content-Type'] = 'application/json'   
    s = requests.Session()
    rs: requests.Response = s.send(r)
    medical_center_dict = rs.json()
    medical_center_dict : MedicalCenter = MedicalCenter(id_address=medical_center_dict['id_medical_center'],
        name=medical_center_dict['name'],
        address=Address(
            id_address=medical_center_dict['address']['id_address'],
            street=medical_center_dict['address']['street'],
            city=medical_center_dict['address']['city']
    ))
    return medical_center_dict