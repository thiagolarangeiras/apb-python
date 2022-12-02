from Options import  EnumStatus
from database import Maintenence

def update():
    cpf = input("CPF: ")
    maintenances = Maintenence.query.filter_by(cpf=cpf)
    if maintenances.count() == 1:
        changeValue(maintenances)
        #saveValue(maintenances[0])
        maintenances.save()
    
    elif maintenances.count() > 1:
        print("\nEscolha um id:")
        for maintenance in maintenances:
            print(f"\t|Cpf: {maintenance.cpf} | Id da manutenção: {maintenance.id}") 
            
        id = int(input("Id: "))
        maintenances = Maintenence.query.filter_by(cpf=cpf,id=id)    
        changeValue(maintenances)
        #saveValue(maintenances[0])
        maintenances[0].save()
        print("A manutenção {} está sendo Atualizada !!!".format(maintenance.id))
    else:
        print("Não existe manutenção nesse status neste cpf!!!")       

def changeValue(maintenance):   
    print("Escolha uma opção")
    print("Detalhes do veiculo:")    
    print("\t1 - Alterar marca.")
    print("\t2 - Alterar modelo.")
    print("\t3 - Alterar cor.")
    print("4 – Alterar valor do orçamento.")
    print("5 - Alterar descrição do serviço.") 
    print("6 - Alterar status.")
    while True:
        option = int(input(""))
        if option == 1:
            maintenance[0].brand = input("Marca: ")
            break
        elif option == 2:
            maintenance[0].model = input("Modelo: ")
            break
        elif option == 3:
            maintenance[0].color = input("Cor: ")
            break
        elif option == 4:
            maintenance[0].value = float(input("Orçamento: "))
            break
        elif option == 5:
            maintenance[0].service_description = input("Descrição do serviço: ")
            break
        elif option == 6:
            maintenance[0].status = str([EnumStatus(input("Tipo do status(Esperando manutenção: A | Em manutenção: M | Cancelada: C | Finalizada: F): ").upper())])
            break

def saveValue(maintenance):
    maintenances = Maintenence.query.filter_by(cpf=maintenance.cpf, id=maintenance.id)   
    maintenances[0].save()
    print(f"A manutenção {maintenance.id} está sendo Atualizada !!!")
    print(maintenance)