from Options import  EnumStatus,EnumReports
from database import manutentions

def get_statusA():
    maintenances =  manutentions.query.filter_by(status=str([EnumStatus.waitingMaintenance]))
    for maintenance in maintenances:
        print("\n{}\n".format(maintenance))
    