from flask import request
import requests
from models.Token import Token
from models.Address import Address
#It defines a method for creating a request that creates an address on the auth_and_admin microservice
def create_address(address:Address,token:Token) -> Address:
        #It prepares the body payload for the POST request for creating the address
        body_payload:dict={
            "street":address.street,
            "city":address.city,
        }
        #It defines the request method (POST) and the URL to be called together with the body specified with Content-Type application/json (json)
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/adreces',json=body_payload)
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
        #print(rs)
        #If the response returns, it tries to parse it in application/json
        address_list = rs.json()
        #print(address_list)
        #If all has gone well, the response has returned an address body in application/json (json) format
        #and it creates an Address instance with the recovered data
        address : Address = Address(
            id_address=address_list['id_address'],
            street=address_list['street'],
            city=address_list['city'],
        )
        #It returns the created address
        return address