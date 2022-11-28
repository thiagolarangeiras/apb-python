from Options import  EnumStatus,EnumReports
from database import manutentions

def get_people():
    cpf = input("CPF: ")
    maintenances =  manutentions.query.filter_by(cpf=cpf)
    for maintenance in maintenances:
        print("\n{}\n".format(maintenance))
       