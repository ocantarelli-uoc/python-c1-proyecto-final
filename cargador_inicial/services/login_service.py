import sys
from flask import request
import requests
from dtos.Token import Token

def login(username:str,password:str) -> Token:
    body_payload:dict={
        "user":username,
        "password":password
    }
    req = requests.post('http://localhost:5001/api/v1/auth/login',json=body_payload)
    r = req.prepare()
    r.headers['Content-Type'] = 'application/json'   
    s = requests.Session()
    rs: requests.Response = s.send(r)
    token_list = rs.json()
    token : Token = Token(token=token_list[0]['token'])
    return token