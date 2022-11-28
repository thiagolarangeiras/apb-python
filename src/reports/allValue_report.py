from Options import  EnumStatus,EnumReports
from database import manutentions

def get_allValue():
    maintenances =  manutentions.query.filter_by(status=str([EnumStatus.finished]))
    value_list = []
    for maintenance in maintenances:
        print("Id:{} --> {}R$".format(maintenance.id,maintenance.value))
        value_list.append(maintenance.value)    
    print("\nTotal:{}R$\n".format(sum(value_list)))