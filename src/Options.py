from enum import Enum

class EnumOptions(Enum):
    Register = 1
    Update = 2
    Perform = 3
    Finalize = 4
    Report = 5
    Close = 6

class EnumVeicleTypes(Enum):
    Car = 'C'
    Bike = 'M'
    Other = 'O'
    
class EnumStatus(Enum):
    waitingMaintenance = 'A'
    onMaintenance =  'M'
    canceled = 'C'
    finished = 'F'
    
class EnumReports(Enum):
    AllReportsMaintenance = 1
    ReportsMaintenanceA = 2
    ReportsMaintenanceM = 3
    ReportsMaintenanceC = 4
    ReportsMaintenanceF = 5
    TotalValueRepots = 6
    PeopleReports = 7
    CloseReports = 8
    

    #List used for storing the maintenace data: its a list of dicts => list(dict()) 
    # the dict shold fallow the MaintenanceData => name is HIGH because showld be a struct
    # maintenances = [
    #     {
    #         "idMaintenance": int() ,
    #         "clientName": str(), 
    #         "cpf": str(), 
    #         "veicleType":  EnumVeicleTypes(),
    #         "details": {
    #             "brand": str(),
    #             "model": str(),
    #             "color": str() 
    #         },
    #         "budget": float(),
    #         "description?": str(),
    #         "entryDate": datetime(),
    #         "exitDate?": datetime(),
    #         "status": EnumStatus()
    #     },
    # ]