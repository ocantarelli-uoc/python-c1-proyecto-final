from enum import Enum

#It defines medical appointment status enum with the needed statuses
class MedicalAppointmentStatusEnum(Enum):
    APPROVED = "Approved"
    DECLINED = "Declined"
    PENDING = "Pending"
    CANCELLED = "Cancelled"