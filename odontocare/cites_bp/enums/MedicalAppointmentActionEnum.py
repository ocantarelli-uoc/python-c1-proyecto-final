from enum import Enum


class MedicalAppointmentActionEnum(Enum):
    CREATE = "Create"
    APPROVE = "Approve"
    DECLINE = "Decline"
    CANCEL = "Cancel"