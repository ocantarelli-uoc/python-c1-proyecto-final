import sys
from flask import request
import requests
from dtos.Token import Token
from dtos.Address import Address
from dtos.MedicalCenter import MedicalCenter

def create_medical_center(medical_center:MedicalCenter,token:Token) -> Address:
    body_payload:dict={
        "name":medical_center.name,
        "id_address":medical_center.address.id_address,
    }
    req = requests.post('http://localhost:5001/api/v1/admin/centres',json=body_payload)
    r = req.prepare()
    r.headers['Authorization'] = token.token
    r.headers['Content-Type'] = 'application/json'
    s = requests.Session()
    rs: requests.Response = s.send(r)
    medical_center_list = rs.json()
    medical_center : MedicalCenter = MedicalCenter(
        id_medical_center=medical_center_list[0]['id_medical_center'],
        address=Address(
            id_address=medical_center_list[0]['address']['id_address'],
            street=medical_center_list[0]['address']['street'],
            city=medical_center_list[0]['address']['city'],
        ),
        name=medical_center_list[0]['name'],
    )
    return medical_center
