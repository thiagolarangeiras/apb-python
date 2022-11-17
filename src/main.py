#!python
import sys
from Options import EnumOptions, EnumVeicleTypes, EnumStatus   
from menu import menu
from maintenance import register 

def alter():
    print("alterar")
def perform():
    print("realizar")
def finalize():
    print("finalizar")
def report():
    print("relatorio")


Options = {
    EnumOptions.Register: register, 
    EnumOptions.Alter: alter,
    EnumOptions.Perform: perform,
    EnumOptions.Finalize: finalize,
    EnumOptions.Report: report
}

def main():
    maintenances = []
    while True:
        option:EnumOptions = menu()
        if option == EnumOptions.Close: 
            break
        a = Options[option](maintenances)
        maintenances.append(a)
        print(maintenances)

if __name__ == "__main__":
    #print("Argumentos de inicialização passados:", sys.argv[1:])
    main()