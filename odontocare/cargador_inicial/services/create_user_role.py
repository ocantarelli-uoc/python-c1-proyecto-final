from flask import request
import requests
from models.Token import Token
from models.UserRole import UserRole

#It defines a method for creating a request that creates a user role (user_role) on the auth_and_admin microservice
def create_user_role(user_role:UserRole,token:Token) -> UserRole:
        #It prepares the body payload for the POST request for creating the user role
        body_payload:dict={
            "role_name":user_role.name,
        }
        #It defines the request method (POST) and the URL to be called together with the body specified with Content-Type application/json (json)
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/rols_usuaris',json=body_payload)
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
        user_role_list = rs.json()
        #If all has gone well, the response has returned a patient body in application/json (json) format
        #and it creates an UserRole instance with the recovered data
        user_role : UserRole = UserRole(
            id_user_role=user_role_list['id_user_role'],
            name=user_role_list['name']
        )
        #It returns the created user role
        return user_role