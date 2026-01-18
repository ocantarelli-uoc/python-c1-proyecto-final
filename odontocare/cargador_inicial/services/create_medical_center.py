from flask import request
import requests
from models.Token import Token
from models.MedicalCenter import MedicalCenter
from models.Address import Address
#It defines a method for creating a request that creates a medical center on the auth_and_admin microservice
def create_medical_center(medical_center:MedicalCenter,token:Token) -> MedicalCenter:
        #It prepares the body payload for the POST request for creating the medical center
        body_payload:dict={
            "name":medical_center.name,
            "id_address":medical_center.address.id_address,
        }
        #It defines the request method (POST) and the URL to be called together with the body specified with Content-Type application/json (json)
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/centres',json=body_payload)
        #It prepares the request with the previous defined configuration
        r = req.prepare()
        #It defines the authorization header (Authorization), specifiying it's of the type Bearer Token, together with the user token
        r.headers['Authorization'] = "Bearer " + token.token
        #It defines the header Content-Type, specifying that the content provided on the body it's of the type application/json (json)
        r.headers['Content-Type'] = 'application/json'
        #It defines the header Accept, which specifies that the client accepts specifically content as response of the type application/json (json)
        r.headers['Accept'] = 'application/json'
        #It starts the request session
        s = requests.Session()
        #It sends the request through the request session, and it gets the response (valid or not)
        rs: requests.Response = s.send(r)
        #If the response returns, it tries to parse it in application/json
        medical_center_list = rs.json()
        #If all has gone well, the response has returned a medical center body in application/json (json) format
        #and it creates an MedicalCenter instance with the recovered data
        medical_center : MedicalCenter = MedicalCenter(
            id_medical_center=medical_center_list['id_medical_center'],
            address=Address(
                id_address=medical_center_list['address']['id_address'],
                street=medical_center_list['address']['street'],
                city=medical_center_list['address']['city'],
            ),
            name=medical_center_list['name'],
        )
        #It returns the created medical center
        return medical_center