from Options import  EnumStatus
from database import Maintenence
from datetime import datetime

def finalize():
    cpf = input("CPF: ")
    maintenances = Maintenence.query.filter_by(cpf=cpf ,status=str([EnumStatus.onMaintenance]))

    if  maintenances.count() == 1:
        changeStatusToFinished(maintenances)

    elif maintenances.count() > 1:
        print("\nEscolha um id:")
        for maintenance in maintenances:
            print(f"\t|Cpf: {maintenance.cpf} | Id da manutenção: {maintenance.id}")  
        id = int(input("Id: "))
        maintenances =  Maintenence.query.filter_by(cpf=cpf, id=id, status=str([EnumStatus.onMaintenance]))
        changeStatusToFinished(maintenances)
    
    else:
        print("Não existe manutenção nesse status neste cpf!!!")       
          
def changeStatusToFinished(maintenances):  
    maintenances[0].status = str([EnumStatus.finished])
    maintenances[0].departure_date = datetime.now()
    maintenances.save()
    date =  maintenances[0].departure_date - maintenances[0].entry_date
    print(f"A manutenção {maintenances[0].id} está sendo Finalizada e durou {date} !!!")
    print(maintenances)