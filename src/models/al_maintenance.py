from Options import  EnumStatus
from database import manutentions


def alter():
    while True:
        cpf = input("CPF: ")
        maintenance_cpf = manutentions.query.filter_by(cpf=cpf)
        maintenance_count = maintenance_cpf.count()
        
        for maintenance_filter in maintenance_cpf:
             id_fl = maintenance_filter.id 
             brand_fl = maintenance_filter.brand
             model_fl =  maintenance_filter.model
             color_fl =  maintenance_filter.color
             value_fl =  maintenance_filter.value
             service_description_fl =  maintenance_filter.service_description
             status_fl =  maintenance_filter.status
             
                 
        if  maintenance_count == 1:
            brand,model,color,value,service_description,status = menu_alter(brand_fl,model_fl,color_fl,value_fl,service_description_fl,status_fl)
            al_manutention(cpf,id_fl,brand,model,color,value,service_description,status)
            break
        elif maintenance_count > 1  :
            print("\nEscolha um id:")
            for maintenance_list in maintenance_cpf:
             print("\t|Cpf: {} | Id da manutenção: {}".format(maintenance_list.cpf, maintenance_list.id)) 
            id = int(input("Id: "))
            maintenance_id = manutentions.query.filter_by(cpf=cpf,id=id)
            for maintenance_filterID in maintenance_id:
             brand_fl = maintenance_filterID.brand
             model_fl =  maintenance_filterID.model
             color_fl =  maintenance_filterID.color
             value_fl =  maintenance_filterID.value
             service_description_fl =  maintenance_filterID.service_description
             status_fl =  maintenance_filterID.status
             
            brand,model,color,value,service_description,status = menu_alter(brand_fl,model_fl,color_fl,value_fl,service_description_fl,status_fl)
            al_manutention(cpf,id,brand,model,color,value,service_description,status)
            break
        else:
            break       
    

def al_manutention(cpf,id,brand,model,color,value,service_description,status):
    maintenances = manutentions.query.filter_by(cpf=cpf)   
   
    for maintenance in maintenances:
        if maintenance.cpf == cpf and maintenance.id == id:
            maintenance.brand = brand
            maintenance.model = model
            maintenance.color = color
            maintenance.value = value
            maintenance.service_description = service_description
            maintenance.status = status
            maintenance.save()
            print("A manutenção {} está sendo Atualizada !!!".format(maintenance.id))
            print(maintenance)
            return True 
        
def menu_alter(brand_fl,model_fl,color_fl,value_fl,service_description_fl,status_fl):
    option = 0 
    brand,model,color,value,service_description,status = brand_fl,model_fl,color_fl,value_fl,service_description_fl,status_fl
    while option !=7:
        
        print(
        """Escolha uma opção :
    Detalhes do veiculo:    
    \t1 - Alterar marca.
    \t2 - Alterar modelo.
    \t3 - Alterar cor.
    4 – Alterar valor do orçamento.
    5 - Alterar descrição do serviço. 
    6 - Alterar status.
    7 – Sair.\n"""
    )
        
        option = int(input("Escolha a opção: "))
        if option == 1:
            brand = input("Marca: ")
        elif option == 2:
            model = input("Modelo: ")
        elif option == 3:
            color = input("Cor: ")
        elif option == 4:
            value = float(input("Orçamento: "))
        elif option == 5:
            service_description = input("Descrição do serviço: ")
        elif option == 6:
            status = str([EnumStatus(input("Tipo do status(Esperando manutenção: A | Em manutenção: M | Cancelada: C | Finalizada: F): ").upper())])
        elif option == 7:
            print("A alteração foi feita com sucesso!!!")
        else:
            print("Essa opção não existe")
        return brand,model,color,value,service_description,status

        
