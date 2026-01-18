from enum import Enum

#It defines medical appointment action enum with the needed actions
class MedicalAppointmentActionEnum(Enum):
    CREATE = "Create"
    APPROVE = "Approve"
    DECLINE = "Decline"
    CANCEL = "Cancel"