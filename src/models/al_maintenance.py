from Options import  EnumStatus
from database import manutentions


def alter():
    while True:
        cpf = input("CPF: ")
        maintenance_cpf = manutentions.query.filter_by(cpf=cpf)
        maintenance_count = maintenance_cpf.count()
        
        for maintenance_filter in maintenance_cpf:
             id_filter = maintenance_filter.id 
                 
        if  maintenance_count == 1:
            al_manutention(cpf,id_filter)
            break
        elif maintenance_count > 1  :
            print("\nEscolha um id:")
            for maintenance_list in maintenance_cpf:
             print("\tCpf: {} / Id da manutenção: {}".format(maintenance_list.cpf, maintenance_list.id)) 
            id = int(input("Id: "))
            al_manutention(cpf,id)
            break
        else:
            break       
    

def al_manutention(cpf,id,brand,model,color,value,service_description,status):
    maintenances = manutentions.query.filter_by(cpf=cpf)   
   
    for maintenance in maintenances:
        if maintenance.cpf == cpf or maintenance.id == id:
            maintenance.brand = brand
            maintenance.model = model
            maintenance.color = color
            maintenance.value = value
            maintenance.service_description = service_description
            maintenance.status = status
            maintenance.save()
            print("A manutenção {} está sendo Atualizada} !!!".format(maintenance.id))
            print(maintenance)
            return True 
        
def menu_alter():
    pass