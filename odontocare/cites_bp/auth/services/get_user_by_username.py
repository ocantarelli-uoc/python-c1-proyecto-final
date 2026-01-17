import sys
from flask import request
import requests
from dtos.User import User
from dtos.UserRole import UserRole

#It defines the method for getting user by username
def get_user_by_username(username:str) -> User:
    #print(username,file=sys.stderr)
    #It does the request to endpoint for getting user by username
    req = requests.Request('GET', 'http://auth_and_admin_bp:5001/api/v1/admin/usuaris/name/'+str(username))
    r = req.prepare()
    r.headers['Authorization'] = request.headers.get('Authorization')
    r.headers['Content-Type'] = 'application/json'
    s = requests.Session()
    #It sends the request and it returns the response
    rs: requests.Response = s.send(r)
    #It parses the response body that it's with json format
    users_list = rs.json()
    #It instances an object of UserRole class for saving the data of user role
    user_role : UserRole = UserRole(id_user_role=users_list[0]['user_role']['id_user_role'],name=users_list[0]['user_role']['name'])
    #It instances an object of User class for saving the data of user
    user : User = User(id_user=users_list[0]['id_user'],username=users_list[0]['username'],user_role=user_role)
    #It returns the user that it's got from auth_and_admin microservice
    return user