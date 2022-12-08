from Options import EnumVeicleTypes, EnumStatus
from database import manutentions


def register():
    while True:
        try:
            name =  input("Nome do titular: ") 
            cpf = input("CPF: ")
            type_vehicle = str([EnumVeicleTypes(input("Tipo do veiculo(carro: C | Moto: M | Outro: O): ").upper())])
            print("Detalhes do veiculo:")
            brand = input("\tMarca: ")
            model = input("\tModelo: ")
            color = input("\tCor: ")
            value = float(input("Orçamento: "))
            service_description = input("Descrição do serviço: ")
            if (name == "" or cpf == "" or brand == "" or model == "" or color == "" or value == "" ):
                raise Exception
            cd_manutention(name,cpf,type_vehicle,brand,model,color,value,service_description)
            break
        except Exception:
            print("\nAviso dados invalidos no ultimo campo inserido!\n")     
          
    return True




def cd_manutention(name,cpf,type_vehicle,brand,model,color,value,service_description,status=str([EnumStatus.waitingMaintenance])):
    
    manutention = manutentions(name=name,cpf=cpf,type_vehicle=type_vehicle
                                  ,brand=brand,model=model,color=color,value=value,
                                   service_description=service_description,status=status)
    manutention.save()
    print('\nMANUTENÇÃO CADASTRADA!')
    print('-' * 20)
    return True
 
 
