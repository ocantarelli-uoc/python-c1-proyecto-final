
import sys
from flask import request
import requests
from converters.AddressConverter import AddressConverter
from converters.DoctorConverter import DoctorConverter
from converters.MedicalAppointmentConverter import MedicalAppointmentConverter
from converters.MedicalAppointmentStatusConverter import MedicalAppointmentStatusConverter
from converters.MedicalCenterConverter import MedicalCenterConverter
from converters.MedicalSpecialityConverter import MedicalSpecialityConverter
from converters.PatientConverter import PatientConverter
from converters.UserConverter import UserConverter
from converters.UserRoleConverter import UserRoleConverter
from util.file_manager import CSVFileManager
from models.Token import Token
from models.Address import Address
from models.User import User
from models.UserRole import UserRole
from models.Doctor import Doctor
from models.MedicalSpeciality import MedicalSpeciality
from models.Patient import Patient
from models.MedicalCenter import MedicalCenter
from models.MedicalAppointmentStatus import MedicalAppointmentStatus
from models.MedicalAppointment import MedicalAppointment
from dotenv import dotenv_values

class CargaInicial:

    def __init__(self,token:Token):
        self.token = token

    def doCharge(self):
        config_dotenv_values = dotenv_values(".env")
        app_first_user_username : str = config_dotenv_values['ADMIN_FIRST_APP_USER_USERNAME']
        app_first_user_password : str = config_dotenv_values['ADMIN_FIRST_APP_USER_PASSWORD']
        token : Token = self.login(app_first_user_username,app_first_user_password)
        self.token = token
        """It instances all the CSV File Managers intances for files and after instance it every one,
        it read its content as a DataFrame with Pandas library
        """
        dadesCsvFileManager = CSVFileManager("data/dades.csv")
        dadesDataFrame = dadesCsvFileManager.read()
        addressConverter = AddressConverter()
        addresses = addressConverter.convert(dadesDataFrame)
        addressConverter.print(addresses)
        medicalCenterConverter = MedicalCenterConverter()
        medical_centers = medicalCenterConverter.convert(dadesDataFrame)
        medicalCenterConverter.print(medical_centers)
        medicalSpecialityConverter = MedicalSpecialityConverter()
        medical_specialities = medicalSpecialityConverter.convert(dadesDataFrame)
        medicalSpecialityConverter.print(medical_specialities)
        userRolesConverter = UserRoleConverter()
        user_roles = userRolesConverter.convert(dadesDataFrame)
        userRolesConverter.print(user_roles)
        userConverter = UserConverter()
        users = userConverter.convert(dadesDataFrame)
        userConverter.print(users)
        patientConverter = PatientConverter()
        patients = patientConverter.convert(dadesDataFrame)
        patientConverter.print(patients)
        doctorConverter = DoctorConverter()
        doctors = doctorConverter.convert(dadesDataFrame)
        doctorConverter.print(doctors)
        medicalAppointmentStatusConverter = MedicalAppointmentStatusConverter()
        medicalAppointmentStatuses = medicalAppointmentStatusConverter.convert(dadesDataFrame)
        medicalAppointmentStatusConverter.print(medicalAppointmentStatuses)
        medicalAppointmentConverter = MedicalAppointmentConverter()
        medicalAppointments = medicalAppointmentConverter.convert(dadesDataFrame)
        medicalAppointmentConverter.print(medicalAppointments)

    
    def create_address(self,address:Address) -> Address:
        body_payload:dict={
            "street":address.street,
            "city":address.city,
        }
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/adreces',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = self.token.token
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
    
    def create_doctor(self,doctor:Doctor) -> Doctor:
        body_payload:dict={
            "username":doctor.user.username,
            "password":doctor.user.password,
            "name":doctor.name,
            "medical_speciality":doctor.medical_speciality.name,
        }
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/doctors',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = self.token.token
        r.headers['Content-Type'] = 'application/json'
        s = requests.Session()
        rs: requests.Response = s.send(r)
        doctors_list = rs.json()
        doctor : Doctor = Doctor(
                    id_doctor=doctors_list[0]['id_doctor'],
                    name=doctors_list[0]['name'],
                    user=User(id_user=doctors_list[0]['user']['id_user'],
                        username=doctors_list[0]['user']['username'],
                        password=doctors_list[0]['user']['password'],
                            user_role=UserRole(
                                id_user_role=doctors_list[0]['user']['user_role']['id_user_role'],
                                name=doctors_list[0]['user']['user_role']['name']
                            )
                    ),
                    medical_speciality=MedicalSpeciality(
                                id_medical_speciality=doctors_list[0]['medical_speciality']['id_medical_speciality'],
                                name=doctors_list[0]['medical_speciality']['name']
                            )
                )
        return doctor
    
    def create_user_role(self,user_role:UserRole) -> UserRole:
        body_payload:dict={
            "role_name":user_role.name,
        }
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/rols_usuaris',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = self.token.token
        r.headers['Content-Type'] = 'application/json'
        s = requests.Session()
        rs: requests.Response = s.send(r)
        user_role_list = rs.json()
        user_role : UserRole = UserRole(
            id_user_role=user_role_list[0]['id_user_role'],
            name=user_role_list[0]['name']
        )
        return user_role
    
    def create_user(self,user:User) -> User:
        body_payload:dict={
            "username":user.username,
            "password":user.password,
            "user_role":user.user_role.name
        }
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/usuaris',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = self.token.token
        r.headers['Content-Type'] = 'application/json'
        s = requests.Session()
        rs: requests.Response = s.send(r)
        user_list = rs.json()
        user : User = User(id_user=user_list[0]['id_user'],
                        username=user_list[0]['username'],
                        password=user_list[0]['password'],
                            user_role=UserRole(
                                id_user_role=user_list[0]['user_role']['id_user_role'],
                                name=user_list[0]['user_role']['name']
                            ) 
                    )
        return user
    
    def create_patient(self,patient:Patient) -> Patient:
        body_payload:dict={
            "username":patient.user.username,
            "password":patient.user.password,
            "name":patient.name,
            "telephone":patient.telephone,
        }
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/pacients',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = self.token.token
        r.headers['Content-Type'] = 'application/json'
        s = requests.Session()
        rs: requests.Response = s.send(r)
        patient_list = rs.json()
        patient : Patient = Patient(
                    id_patient=patient_list[0]['id_patient'],
                    name=patient_list[0]['name'],
                    telephone=patient_list[0]['telephone'],
                    is_active=patient_list[0]['is_active'],
                    user=User(id_user=patient_list[0]['user']['id_user'],
                        username=patient_list[0]['user']['username'],
                        password=patient_list[0]['user']['password'],
                            user_role=UserRole(
                                id_user_role=patient_list[0]['user']['user_role']['id_user_role'],
                                name=patient_list[0]['user']['user_role']['name']
                            )
                    )
                )
        return patient
    
    def create_medical_center(self,medical_center:MedicalCenter) -> Address:
        body_payload:dict={
            "name":medical_center.name,
            "id_address":medical_center.address.id_address,
        }
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/centres',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = self.token.token
        r.headers['Content-Type'] = 'application/json'
        s = requests.Session()
        rs: requests.Response = s.send(r)
        medical_center_list = rs.json()
        medical_center : MedicalCenter = MedicalCenter(
            id_medical_center=medical_center_list[0]['id_medical_center'],
            address=Address(
                id_address=medical_center_list[0]['address']['id_address'],
                street=medical_center_list[0]['address']['street'],
                city=medical_center_list[0]['address']['city'],
            ),
            name=medical_center_list[0]['name'],
        )
        return medical_center
    
    def create_medical_speciality(self,medical_speciality:MedicalSpeciality) -> MedicalSpeciality:
        body_payload:dict={
            "medical_speciality_name":medical_speciality.name,
        }
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/admin/especialitats_mediques',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = self.token.token
        r.headers['Content-Type'] = 'application/json'
        s = requests.Session()
        rs: requests.Response = s.send(r)
        medical_speciality_list = rs.json()
        medical_speciality : MedicalSpeciality = MedicalSpeciality(
            id_medical_speciality=medical_speciality_list[0]['id_medical_speciality'],
            name=medical_speciality_list[0]['name'],
        )
        return medical_speciality
    
    def create_medical_appointment_status(self,medical_appointment_status:MedicalAppointmentStatus) -> MedicalAppointmentStatus:
        body_payload:dict={
            "status_name":medical_appointment_status.name,
        }
        req = requests.Request('POST','http://cites_bp:5002/api/v1/admin/estats_cites',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = self.token.token
        r.headers['Content-Type'] = 'application/json'
        s = requests.Session()
        rs: requests.Response = s.send(r)
        medical_appointment_status_list = rs.json()
        medical_appointment_status : MedicalAppointmentStatus = MedicalAppointmentStatus(
            id_medical_status=medical_appointment_status_list[0]['id_medical_status'],
            name=medical_appointment_status_list[0]['name'],
        )
        return medical_appointment_status
    
    def create_medical_appointment(self,medical_appointment:MedicalAppointment) -> MedicalAppointment:
        body_payload:dict={
            "appointment_date":str(medical_appointment.appointment_date),
            "id_doctor":medical_appointment.id_doctor,
            "id_patient":medical_appointment.id_patient,
            "id_medical_center":medical_appointment.id_medical_center,
            "motiu":medical_appointment.motiu,
            "id_action_user":medical_appointment.id_action_user,
        }
        req = requests.Request('POST','http://cites_bp:5002/api/v1/admin/cites',json=body_payload)
        r = req.prepare()
        r.headers['Authorization'] = self.token.token
        r.headers['Content-Type'] = 'application/json'
        s = requests.Session()
        rs: requests.Response = s.send(r)
        medical_appointment_list = rs.json()
        medical_appointment : MedicalAppointment = MedicalAppointment(
            id_medical_appointment=None,
            medical_status=None,
            id_doctor=medical_appointment_list[0]['id_doctor'],
            id_patient=medical_appointment_list[0]['id_patient'],
            id_medical_center=medical_appointment_list[0]['id_medical_center'],
            appointment_date=medical_appointment_list[0]['appointment_date'],
            motiu=medical_appointment_list[0]['motiu'],
            id_action_user=medical_appointment_list[0]['id_action_user'],
        )
        return medical_appointment
    
    def login(self,username:str,password:str) -> Token:
        body_payload:dict={
            "user":username,
            "password":password
        }
        req = requests.Request('POST','http://auth_and_admin_bp:5001/api/v1/auth/login',json=body_payload)
        r = req.prepare()
        r.headers['Content-Type'] = 'application/json'   
        s = requests.Session()
        rs: requests.Response = s.send(r)
        token_list = rs.json()
        token : Token = Token(token=token_list['token'])
        print(token)
        return token