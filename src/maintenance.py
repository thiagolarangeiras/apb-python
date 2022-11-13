from Options import EnumVeicleTypes, EnumStatus
from datetime import datetime

def register(maintenances)->int:
    while True:
        try:
            newRegister = {}
            newRegister["idMaintenance"] = (maintenances[-1]["idMaintenance"] + 1) if (len(maintenances) > 0) else (1)  
            newRegister["clientName"] = input("Nome do titular: ") 
            newRegister["cpf"] = input("CPF: ")
            newRegister["veicleType"] =  EnumVeicleTypes(input("Tipo do veiculo(carro: C | Moto: M | Outro: O): ").upper())
            print("Detalhes do veiculo:")
            newRegister["details"] = {}
            newRegister["details"]["brand"] = input("\tMarca: ") 
            newRegister["details"]["model"] = input("\tModelo: ")
            newRegister["details"]["color"] = input("\tCor: ")
            newRegister["budget"] =  float(input("Orçamento: "))
            newRegister["description?"] = input("Descrição do serviço: ")
            newRegister["entryDate"] = datetime.now()
            newRegister["exitDate?"] = datetime.min
            newRegister["status"] = EnumStatus.waitingMaintenance
            maintenances.append(newRegister) 
            print("\nCadastro Realizado com sucesso!\n")
            break
        except:
            print("\nAviso dados invalidos no ultimo campo inserido!\n")    
def 