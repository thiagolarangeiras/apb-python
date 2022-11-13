#!python
import sys
from Options import EnumOptions, EnumVeicleTypes, EnumStatus   
from menu import menu
from maintenance import register 

def main():
    while True:
        maintenances = []
        Options = {
            EnumOptions.Register: register, 
        }
        option:EnumOptions = menu()
        if option == EnumOptions.Close: 
            break
        Options[option](maintenances)

if __name__ == "__main__":
    #print("Argumentos de inicialização passados:", sys.argv[1:])
    main()