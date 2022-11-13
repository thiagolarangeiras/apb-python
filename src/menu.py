from Options import EnumOptions   

def menu()->EnumOptions:
    printOptions()
    option:EnumOptions = getOption()
    return option

def printOptions()->None:
    print(
        """Escolha uma opção :
    1 - Cadastrar Manutenção.
    2 - Alterar Manutenção.
    3 - Realizar Manutenção.
    4 – Finalizar Manutenção.
    5 - Relatórios. 
    6 – Sair.\n"""
    )

def getOption()->EnumOptions: 
    while True:
        try:
            option = EnumOptions(int(input("Escolha: ")))
            return option
        except:
            pass #se não for valido aguarda até resposta valida