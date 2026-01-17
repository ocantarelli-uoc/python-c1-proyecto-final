from flask import request
import requests
from models.Token import Token
from models.MedicalSpeciality import MedicalSpeciality

def create_medical_speciality(medical_speciality:MedicalSpeciality,token:Token) -> MedicalSpeciality:
        body_payload:dict={
            "medical_speciality_name":medical_speciality.name,
        }
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/especialitats_mediques',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = "Bearer " + token.token
        r.headers['Content-Type'] = 'application/json'
        s = requests.Session()
        rs: requests.Response = s.send(r)
        medical_speciality_list = rs.json()
        medical_speciality : MedicalSpeciality = MedicalSpeciality(
            id_medical_speciality=medical_speciality_list['id_medical_speciality'],
            name=medical_speciality_list['name'],
        )
        return medical_speciality