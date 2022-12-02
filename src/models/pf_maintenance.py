from Options import  EnumStatus
from database import Maintenence

def perform():
    while True:
        cpf = input("CPF: ")
        maintenance_cpf = Maintenence.query.filter_by(cpf=cpf ,status=str([EnumStatus.waitingMaintenance]))
        st = maintenance_cpf[0].status
        
        if  maintenance_cpf.count() == 1:
            id_filter = maintenance_cpf.id 
            rl_manutention(cpf,id_filter)
            break

        elif maintenance_cpf.count() > 1 and st == str([EnumStatus.waitingMaintenance]) :
            print("\nEscolha um id:")
            for maintenance_list in maintenance_cpf:
             print("\t|Cpf: {} | Id da manutenção: {}".format(maintenance_list.cpf, maintenance_list.id))  
            id = int(input("Id: "))
            rl_manutention(cpf,id)
            break
        
        else:
            print("Não existe manutenção nesse status neste cpf!!!")
            break       
          
def rl_manutention(cpf,id):  
    maintenances =  Maintenence.query.filter_by(cpf=cpf,status=str([EnumStatus.waitingMaintenance]))
    for maintenance in maintenances:
        if maintenance.cpf == cpf and maintenance.id == id:
            maintenance.status = str([EnumStatus.onMaintenance])
            maintenance.save()
            print("A manutenção {} está sendo iniciada !!!".format(maintenance.id))
            print(maintenance)
            return True 
       
               

         