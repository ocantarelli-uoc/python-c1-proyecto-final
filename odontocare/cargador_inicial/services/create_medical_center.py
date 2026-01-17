from flask import request
import requests
from models.Token import Token
from models.MedicalCenter import MedicalCenter
from models.Address import Address

def create_medical_center(medical_center:MedicalCenter,token:Token) -> Address:
        body_payload:dict={
            "name":medical_center.name,
            "id_address":medical_center.address.id_address,
        }
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/centres',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = "Bearer " + token.token
        r.headers['Content-Type'] = 'application/json'
        s = requests.Session()
        rs: requests.Response = s.send(r)
        medical_center_list = rs.json()
        medical_center : MedicalCenter = MedicalCenter(
            id_medical_center=medical_center_list['id_medical_center'],
            address=Address(
                id_address=medical_center_list['address']['id_address'],
                street=medical_center_list['address']['street'],
                city=medical_center_list['address']['city'],
            ),
            name=medical_center_list['name'],
        )
        return medical_center