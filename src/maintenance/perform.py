from Options import  EnumStatus
from database import Maintenence

def perform():
    cpf = input("CPF: ")
    maintenances = Maintenence.query.filter_by(cpf=cpf ,status=str([EnumStatus.waitingMaintenance]))

    if  maintenances.count() == 1:
        changeStatusToOnMaintenance(maintenances)
    elif maintenances.count() > 1:
        print("\nEscolha um id:")
        for maintenance in maintenances:
            print(f"\t|Cpf: {maintenance.cpf} | Id da manutenção: {maintenance.id}")  
        id = int(input("Id: "))
        maintenances =  Maintenence.query.filter_by(cpf=cpf, id=id, status=str([EnumStatus.waitingMaintenance]))
        changeStatusToOnMaintenance(maintenances)
    else:
        print("Não existe manutenção nesse status neste cpf!!!")       
          
def changeStatusToOnMaintenance(maintenances):  
    maintenances[0].status = str([EnumStatus.onMaintenance])
    maintenances[0].save()
    print(f"A manutenção {maintenances.id} está sendo iniciada !!!")
    print(maintenances)
       
               

         