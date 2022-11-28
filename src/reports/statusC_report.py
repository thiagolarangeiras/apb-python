from Options import  EnumStatus,EnumReports
from database import manutentions

def get_statusC():
    maintenances =  manutentions.query.filter_by(status=str([EnumStatus.canceled]))
    for maintenance in maintenances:
        print("\n{}\n".format(maintenance))