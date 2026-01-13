import sys
from flask import request
import requests
from dtos.Token import Token
from dtos.MedicalSpeciality import MedicalSpeciality

def create_medical_speciality(medical_speciality:MedicalSpeciality,token:Token) -> MedicalSpeciality:
    body_payload:dict={
        "medical_speciality_name":medical_speciality.name,
    }
    req = requests.post('http://localhost:5001/api/v1/admin/especialitats_mediques',json=body_payload)
    r = req.prepare()
    r.headers['Authorization'] = token.token
    r.headers['Content-Type'] = 'application/json'
    s = requests.Session()
    rs: requests.Response = s.send(r)
    medical_speciality_list = rs.json()
    medical_speciality : MedicalSpeciality = MedicalSpeciality(
        id_medical_speciality=medical_speciality_list[0]['id_medical_speciality'],
        name=medical_speciality_list[0]['name'],
    )
    return medical_speciality
