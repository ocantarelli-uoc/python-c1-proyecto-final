
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
from dtos.MedicalAppointment import MedicalAppointment
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
        """It instances all the CSV File Manager intance for file dades.csv and after instance it,
        it read its content as a DataFrame with Pandas library
        """
        dadesCsvFileManager = CSVFileManager("data/dades.csv")
        dadesDataFrame = dadesCsvFileManager.read()
        #It instances the address converter
        addressConverter = AddressConverter()
        #It converts the rows from dades.csv data frame which are addresses
        addresses = addressConverter.convert(dadesDataFrame)
        #addressConverter.print(addresses)
        #It instances the medical center converter
        medicalCenterConverter = MedicalCenterConverter()
        #It converts the rows from dades.csv data frame which are medical centers
        medical_centers = medicalCenterConverter.convert(dadesDataFrame)
        #medicalCenterConverter.print(medical_centers)
        #It instances the medical speciality converter
        medicalSpecialityConverter = MedicalSpecialityConverter()
        #It converts the rows from dades.csv data frame which are medical specialities
        medical_specialities = medicalSpecialityConverter.convert(dadesDataFrame)
        #medicalSpecialityConverter.print(medical_specialities)
        #It instances the user role converter
        userRolesConverter = UserRoleConverter()
        #It converts the rows from dades.csv data frame which are user roles
        user_roles = userRolesConverter.convert(dadesDataFrame)
        #userRolesConverter.print(user_roles)
        #It instances the user converter
        userConverter = UserConverter()
        #It converts the rows from dades.csv data frame which are users
        users = userConverter.convert(dadesDataFrame)
        #userConverter.print(users)
        #It instances the patient converter
        patientConverter = PatientConverter()
        #It converts the rows from dades.csv data frame which are patients
        patients = patientConverter.convert(dadesDataFrame)
        #patientConverter.print(patients)
        #It instances the doctor converter
        doctorConverter = DoctorConverter()
        #It converts the rows from dades.csv data frame which are doctors
        doctors = doctorConverter.convert(dadesDataFrame)
        #doctorConverter.print(doctors)
        #It instances the medical appointment status converter
        medicalAppointmentStatusConverter = MedicalAppointmentStatusConverter()
        #It converts the rows from dades.csv data frame which are medical appointment statuses
        medicalAppointmentStatuses = medicalAppointmentStatusConverter.convert(dadesDataFrame)
        #medicalAppointmentStatusConverter.print(medicalAppointmentStatuses)
        #It instances the medical appointment converter
        medicalAppointmentConverter = MedicalAppointmentConverter()
        #It converts the rows from dades.csv data frame which are medical appointments
        medicalAppointments = medicalAppointmentConverter.convert(dadesDataFrame)
        #medicalAppointmentConverter.print(medicalAppointments)
        #It creates every address
        for address in addresses:
            create_address(address=address,token=token)
        #It creates every medical center
        for medical_center in medical_centers:
            create_medical_center(medical_center=medical_center,token=token)
        #It creates every medical speciality
        for medical_speciality in medical_specialities:
            create_medical_speciality(medical_speciality=medical_speciality,token=token)
        #It creates every user role
        for user_role in user_roles:
            create_user_role(user_role=user_role,token=token)
        #It creates every user
        for user in users:
            create_user(user=user,token=token)
        #It creates every patient
        for patient in patients:
            create_patient(patient=patient,token=token)
        #It creates every doctor
        for doctor in doctors:
            create_doctor(doctor=doctor,token=token)
        #It creates every medical appointment status
        for medical_appointment_status in medicalAppointmentStatuses:
            create_medical_appointment_status(medical_appointment_status=medical_appointment_status,token=token)
        #It creates every medical appointment
        for medical_appointment in medicalAppointments:
            created_medical_appointment : MedicalAppointment = create_medical_appointment(medical_appointment=medical_appointment,token=token)
            #print(created_medical_appointment.describe())