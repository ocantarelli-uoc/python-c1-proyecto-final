from flask import request
import requests
from models.Token import Token
from models.Address import Address
def create_address(address:Address,token:Token) -> Address:
        body_payload:dict={
            "street":address.street,
            "city":address.city,
        }
        #print(body_payload)
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/adreces',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = "Bearer " + token.token
        r.headers['Content-Type'] = 'application/json'
        r.headers['Accept'] = 'application/json'
        s = requests.Session()
        rs: requests.Response = s.send(r)
        #print(rs)
        address_list = rs.json()
        #print(address_list)
        address : Address = Address(
            id_address=address_list['id_address'],
            street=address_list['street'],
            city=address_list['city'],
        )
        return address