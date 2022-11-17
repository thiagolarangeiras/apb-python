#!python
import sys
from Options import EnumOptions, EnumVeicleTypes, EnumStatus   
from menu import menu
from maintenance import register 

Options = {
    EnumOptions.Register: register, 
    EnumOptions.Alter: alter,
    EnumOptions.Perform = perform,
    EnumOptions.Finalize = finalize,
    EnumOptions.Report = report,
    EnumOptions.Close = close
}

def main():
    while True:
        maintenances = []
        option:EnumOptions = menu()
        if option == EnumOptions.Close: 
            break
        Options[option](maintenances)

if __name__ == "__main__":
    #print("Argumentos de inicialização passados:", sys.argv[1:])
    main()