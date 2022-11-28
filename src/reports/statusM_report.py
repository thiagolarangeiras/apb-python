from Options import  EnumStatus,EnumReports
from database import manutentions

def get_statusM():
    maintenances =  manutentions.query.filter_by(status=str([EnumStatus.onMaintenance]))
    for maintenance in maintenances:
        print("\n{}\n".format(maintenance))