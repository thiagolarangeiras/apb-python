from Options import  EnumStatus,EnumReports
from database import manutentions

def get_all():
    maintenances =  manutentions.query.all()
    for maintenance in maintenances:
        print("\n{}\n".format(maintenance))