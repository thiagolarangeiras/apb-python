from Options import EnumVeicleTypes, EnumStatus
from database import Maintenence

def insert():
    while True:
        try:
            maintenence = Maintenence()
            maintenence.name =  input("Nome do titular: ") 
            maintenence.cpf = input("CPF: ")
            maintenence.type_vehicle = str([EnumVeicleTypes(input("Tipo do veiculo(carro: C | Moto: M | Outro: O): ").upper())])
            print("Detalhes do veiculo:")
            maintenence.brand = input("\tMarca: ")
            maintenence.model = input("\tModelo: ")
            maintenence.color = input("\tCor: ")
            maintenence.value = float(input("Orçamento: "))
            maintenence.service_description = input("Descrição do serviço: ")
            maintenence.status=str([EnumStatus.waitingMaintenance])
            if (maintenence.name == "" or maintenence.cpf == "" or maintenence.brand == "" or maintenence.model == "" or maintenence.color == "" or maintenence.value == "" ):
                raise Exception
            
            maintenence.save()
            print(' MANUTENÇÃO CADASTRADA!')
            print(maintenence)
            print('-' * 90)
            break
        except:
            print("\nAviso dados invalidos no ultimo campo inserido!\n")