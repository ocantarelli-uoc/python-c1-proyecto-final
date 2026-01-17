
import sys
import json
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
from services.create_address import create_address
from services.create_medical_center import create_medical_center
from services.create_medical_speciality import create_medical_speciality
from services.login import login
from services.create_user import create_user
from services.create_patient import create_patient
from services.create_doctor import create_doctor
from services.create_user_role import create_user_role
from services.create_medical_appointment_status import create_medical_appointment_status
from services.create_medical_appointment import create_medical_appointment
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
        token : Token = login(app_first_user_username,app_first_user_password)
        self.token = token
        """It instances all the CSV File Managers intances for files and after instance it every one,
        it read its content as a DataFrame with Pandas library
        """
        dadesCsvFileManager = CSVFileManager("data/dades.csv")
        dadesDataFrame = dadesCsvFileManager.read()
        addressConverter = AddressConverter()
        addresses = addressConverter.convert(dadesDataFrame)
        #addressConverter.print(addresses)
        medicalCenterConverter = MedicalCenterConverter()
        medical_centers = medicalCenterConverter.convert(dadesDataFrame)
        #medicalCenterConverter.print(medical_centers)
        medicalSpecialityConverter = MedicalSpecialityConverter()
        medical_specialities = medicalSpecialityConverter.convert(dadesDataFrame)
        #medicalSpecialityConverter.print(medical_specialities)
        userRolesConverter = UserRoleConverter()
        user_roles = userRolesConverter.convert(dadesDataFrame)
        #userRolesConverter.print(user_roles)
        userConverter = UserConverter()
        users = userConverter.convert(dadesDataFrame)
        #userConverter.print(users)
        patientConverter = PatientConverter()
        patients = patientConverter.convert(dadesDataFrame)
        #patientConverter.print(patients)
        doctorConverter = DoctorConverter()
        doctors = doctorConverter.convert(dadesDataFrame)
        #doctorConverter.print(doctors)
        medicalAppointmentStatusConverter = MedicalAppointmentStatusConverter()
        medicalAppointmentStatuses = medicalAppointmentStatusConverter.convert(dadesDataFrame)
        #medicalAppointmentStatusConverter.print(medicalAppointmentStatuses)
        medicalAppointmentConverter = MedicalAppointmentConverter()
        medicalAppointments = medicalAppointmentConverter.convert(dadesDataFrame)
        #medicalAppointmentConverter.print(medicalAppointments)

        for address in addresses:
            create_address(address=address,token=token)
        
        for medical_center in medical_centers:
            create_medical_center(medical_center=medical_center,token=token)
        
        for medical_speciality in medical_specialities:
            create_medical_speciality(medical_speciality=medical_speciality,token=token)
        
        for user_role in user_roles:
            create_user_role(user_role=user_role,token=token)
        
        for user in users:
            create_user(user=user,token=token)

        for patient in patients:
            create_patient(patient=patient,token=token)
        
        for doctor in doctors:
            create_doctor(doctor=doctor,token=token)
        
        for medical_appointment_status in medicalAppointmentStatuses:
            create_medical_appointment_status(medical_appointment_status=medical_appointment_status,token=token)
        
        for medical_appointment in medicalAppointments:
            created_medical_appointment : MedicalAppointment = create_medical_appointment(medical_appointment=medical_appointment,token=token)
            #print(created_medical_appointment.describe())