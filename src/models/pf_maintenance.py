from Options import  EnumStatus
from database import manutentions

def perform():
    while True:
        cpf = input("CPF: ")
        maintenance_cpf = manutentions.query.filter_by(cpf=cpf ,status=str([EnumStatus.waitingMaintenance]))
        maintenance_count = maintenance_cpf.count()
        
        for maintenance_filter in maintenance_cpf:
             id_filter = maintenance_filter.id 
             st = maintenance_filter.status
             
        if  maintenance_count == 1:
            rl_manutention(cpf,id_filter)
            break
        elif maintenance_count > 1 and st == str([EnumStatus.waitingMaintenance]) :
            print("\nEscolha um id:")
            for maintenance_list in maintenance_cpf:
             print("\tCpf: {} / Id da manutenção: {}".format(maintenance_list.cpf, maintenance_list.id)) 
            id = int(input("Id: "))
            rl_manutention(cpf,id)
            break
        else:
            break       
          
def rl_manutention(cpf,id):  
    maintenances =  manutentions.query.filter_by(cpf=cpf,status=str([EnumStatus.waitingMaintenance]))
    for maintenance in maintenances:
        if maintenance.cpf == cpf or maintenance.id == id:
            maintenance.status = str([EnumStatus.onMaintenance])
            maintenance.save()
            print("A manutenção {} está sendo iniciada !!!".format(maintenance.id))
            print(maintenance)
            return True 
       
               

         