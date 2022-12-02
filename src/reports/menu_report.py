from Options import EnumStatus, EnumReports

def menu_reports()->EnumReports:
    printOptions()
    option:EnumReports = getOption()
    return option

def printOptions()->None:
    print(
        """Escolha uma opção :
    1 - Relatório de todas as manutenções.
    2 - Relatório de todas as manutenções com status A.
    3 - Relatório de todas as manutenções com status M.
    4 – Relatório de todas as manutenções com status C.
    5 - Relatório de todas as manutenções com status F.
    6 – Relatório total recebido.
    7 - Relatório de manutenções por pessooa.
    8 - Sair.\n"""          
    )

def getOption()->EnumReports: 
    while True:
        try:
            option = EnumReports(int(input("Escolha: ")))
            return option
        except:
            pass #se não for valido aguarda até resposta valida
         