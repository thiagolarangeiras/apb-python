from Options import  EnumStatus,EnumReports
from database import manutentions

def get_statusF():
    maintenances =  manutentions.query.filter_by(status=str([EnumStatus.finished]))
    for maintenance in maintenances:
        print("\n{}\n".format(maintenance))