from Options import EnumVeicleTypes, EnumStatus
from datetime import datetime

def register(maintenances)->int:
    while True:
        try:
            newRegister = {}
            newRegister["idMaintenance"] = (maintenances[-1]["idMaintenance"] + 1) if (len(maintenances) > 0) else (1)  
            newRegister["clientName"] = input("Nome do titular: ") 
            if newRegister["clientName"] == '':
                raise Exception
            newRegister["cpf"] = input("CPF: ")
            if newRegister["cpf"] == '':
                raise Exception
            newRegister["veicleType"] =  EnumVeicleTypes(input("Tipo do veiculo(carro: C | Moto: M | Outro: O): ").upper())
            print("Detalhes do veiculo:")
            newRegister["details"] = {}
            newRegister["details"]["brand"] = input("\tMarca: ") 
            if newRegister["details"]["brand"] == '':
                raise Exception
            newRegister["details"]["model"] = input("\tModelo: ")
            if newRegister["details"]["model"] == '':
                raise Exception
            newRegister["details"]["color"] = input("\tCor: ")
            if newRegister["details"]["color"] == '':
                raise Exception
            newRegister["budget"] =  float(input("Orçamento: "))
            if newRegister["budget"] == '':
                raise Exception
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