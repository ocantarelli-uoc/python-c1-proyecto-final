from enum import Enum


class MedicalAppointmentStatusEnum(Enum):
    APPROVED = "Approved"
    DECLINED = "Declined"
    PENDING = "Pending"
    CANCELLED = "Cancelled"