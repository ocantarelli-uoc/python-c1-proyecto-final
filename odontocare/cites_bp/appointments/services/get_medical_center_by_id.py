import sys
from flask import request
import requests
from dtos.MedicalCenter import MedicalCenter
from dtos.Address import Address

#It defines the method for getting medical center by id
def get_medical_center_by_id(id:int) -> MedicalCenter:
    #print(id,file=sys.stderr)
    #It does the request for getting medical center by id to auth_and_admin microservice
    req = requests.Request('GET', 'http://auth_and_admin_bp:5001/api/v1/admin/centres/'+str(id))
    r = req.prepare()
    r.headers['Authorization'] = request.headers.get('Authorization')
    r.headers['Content-Type'] = 'application/json'   
    s = requests.Session()
    #It sends the request and it gets the response
    rs: requests.Response = s.send(r)
    #It parses patient json response
    medical_center_list = rs.json()
    medical_center = None
    #It checks if the recovered response it's a list
    if medical_center_list is not None and isinstance(medical_center_list,list) and len(medical_center_list) >= 1:
        #It gets the medical center from response
        medical_center : MedicalCenter = MedicalCenter(id_medical_center=medical_center_list[0]['id_medical_center'],
            name=medical_center_list[0]['name'],
            address=Address(
                id_address=medical_center_list[0]['address']['id_address'],
                street=medical_center_list[0]['address']['street'],
                city=medical_center_list[0]['address']['city']
        ))
    #It returns the medical center
    return medical_center