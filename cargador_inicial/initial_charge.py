

from cargador_inicial.util.file_manager import CSVFileManager


class InitialCharger:

    def doCharge(self):
        """It instances all the CSV File Managers intances for files and after instance it every one,
        it read its content as a DataFrame with Pandas library
        """
        addressesCsvFileManager = CSVFileManager("data/addresses.csv")
        addressesDataFrame = addressesCsvFileManager.read()
        medicalCentersCsvFileManager = CSVFileManager("data/medical_centers.csv")
        medicalCentersDataFrame = medicalCentersCsvFileManager.read()
        medicalSpecialitiesCsvFileManager = CSVFileManager("data/medical_specialities.csv")
        medicalSpecialitiesDataFrame = medicalSpecialitiesCsvFileManager.read()
        userRolesCsvFileManager = CSVFileManager("data/user_roles.csv")
        userRolesDataFrame = userRolesCsvFileManager.read()
        usersCsvFileManager = CSVFileManager("data/users.csv")
        usersDataFrame = usersCsvFileManager.read()
        doctorsCsvFileManager = CSVFileManager("data/doctors.csv")
        doctorsDataFrame = doctorsCsvFileManager.read()
        patientsCsvFileManager = CSVFileManager("data/patients.csv")
        patientsDataFrame = patientsCsvFileManager.read()