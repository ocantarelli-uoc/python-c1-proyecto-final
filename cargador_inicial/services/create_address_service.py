import sys
from flask import request
import requests
from dtos.Token import Token
from dtos.Address import Address

def create_address(address:Address,token:Token) -> Address:
    body_payload:dict={
        "street":address.street,
        "city":address.city,
    }
    req = requests.post('http://localhost:5001/api/v1/admin/adreces',json=body_payload)
    r = req.prepare()
    r.headers['Authorization'] = token.token
    r.headers['Content-Type'] = 'application/json'
    s = requests.Session()
    rs: requests.Response = s.send(r)
    address_list = rs.json()
    address : Address = Address(
        id_address=address_list[0]['id_address'],
        street=address_list[0]['street'],
        city=address_list[0]['city'],
    )
    return address
