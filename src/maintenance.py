from Options import EnumVeicleTypes, EnumStatus
from datetime import datetime

def register(maintenances)->dict:
    newRegister = {}
    while True:
        try:
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
            print("a")
            newRegister["entryDate"] = datetime.now()
            print("b")
            newRegister["exitDate?"] = datetime.min
            print("c")
            newRegister["status"] = EnumStatus.waitingMaintenance 
            print("\nCadastro Realizado com sucesso!\n")
            break
        except:
            print("\nAviso dados invalidos no ultimo campo inserido!\n")     
    maintenances.append(newRegister)

def alter():
    print("alterar")

def perform(maintenances):
    # Buscar manutenção por cpf
    cpfSearch = input('\nCPF do cliente: ')

    maintenancesFounded = [] # manutenções do cliente

    print('\nManutenções encontradas:')
    for maintenance in maintenances:
        if maintenance['cpf'] == cpfSearch:
            print(maintenance)
            maintenancesFounded.append(maintenance)
        
    # Verificando a quantidade de manutenções encontradas
    if len(maintenancesFounded) == 0:
        print('\nNão foram encontradas manutenções no CPF informado.\n')
        return
    elif len(maintenancesFounded) > 1:
        # Escolha da manutenção pelo id 
        maintenanceID = input('\nID da manutenção que deseja realizar: ')
    else:
        maintenanceID = maintenancesFounded[0]['idMaintenance']
        
    # Iniciando a manutenção
    for index in range(len(maintenances)):
        if maintenances[index]['idMaintenance'] == maintenanceID:
            maintenances[index]['status'] = EnumStatus.onMaintenance
            print(f'\nA manutenção (id:{maintenanceID}) está sendo iniciada!\n')
    

def finalize(maintenances):
     # Buscar manutenção por cpf
    cpfSearch = input('\nCPF do cliente: ')

    maintenancesFounded = [] # manutenções do cliente

    print('\nManutenções encontradas:')
    for maintenance in maintenances:
        if maintenance['cpf'] == cpfSearch and maintenance['status'] == EnumStatus.onMaintenance:
            print(maintenance)
            maintenancesFounded.append(maintenance)
            
    # Verificando a quantidade de manutenções encontradas
    if len(maintenancesFounded) == 0:
        print('\nNão foram encontradas manutenções já iniciadas no CPF informado.\n')
        return
    elif len(maintenancesFounded) > 1:
        # Escolha da manutenção pelo id 
        maintenanceID = input('\nID da manutenção que deseja finalizar: ')
    else:
        maintenanceID = maintenancesFounded[0]['idMaintenance']
        
    # Finalizando a manutenção
    for index in range(len(maintenances)):
        if maintenances[index]['idMaintenance'] == maintenanceID:
            maintenances[index]['status'] = EnumStatus.onMaintenance
            maintenances[index]["exitDate?"] = datetime.now()
            durationTime = maintenances[index]["entryDate"] - maintenances[index]['exitDate?']
            print(f'\nA manutenção (id:{maintenanceID}) foi finalizada com sucesso! Ela durou cerca de {durationTime} dias\n')
    

def report():
    print("relatorio")