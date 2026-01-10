from enum import Enum


class UserRoleEnum(Enum):
    ADMIN = "admin"
    SECRETARY = "secretary"
    DOCTOR = "doctor"
    PATIENT = "patient"