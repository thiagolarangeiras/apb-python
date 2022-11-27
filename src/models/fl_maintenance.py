from Options import  EnumStatus
from database import manutentions
from datetime import datetime

def finalize():
    while True:
        cpf = input("CPF: ")
        maintenance_cpf = manutentions.query.filter_by(cpf=cpf,status=str([EnumStatus.onMaintenance]))
        maintenance_count = maintenance_cpf.count()
        
        for maintenance_filter in maintenance_cpf:
             id_filter = maintenance_filter.id 
             st = maintenance_filter.status
             
        if  maintenance_count == 1:
            fl_manutention(cpf,id_filter)
            break
        elif maintenance_count > 1 and st == str([EnumStatus.onMaintenance]) :
            print("\nEscolha um id:")
            for maintenance_list in maintenance_cpf:
             print("\tCpf: {} / Id da manutenção: {}".format(maintenance_list.cpf, maintenance_list.id)) 
            id = int(input("Id: "))
            fl_manutention(cpf,id)
            break
        else:
            break       
    

def fl_manutention(cpf,id):
    maintenances = manutentions.query.filter_by(cpf=cpf,status=str([EnumStatus.onMaintenance]))   
   
    for maintenance in maintenances:
        if maintenance.cpf == cpf or maintenance.id == id:
            maintenance.status = str([EnumStatus.finished])
            maintenance.departure_date = datetime.now()
            maintenance.save()
            date =  maintenance.departure_date - maintenance.entry_date
            print("A manutenção {} está sendo Finalizada e durou {} !!!".format(maintenance.id,date))
            print(maintenance)
            return True 