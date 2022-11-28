#!python
import sys
from Options import EnumOptions, EnumVeicleTypes, EnumStatus   
from menu import menu
from models.maintenance import register 
from models.pf_maintenance import perform
from models.fl_maintenance import finalize
from models.al_maintenance import alter
from reports.report import report




Options = {
    EnumOptions.Register: register, 
    EnumOptions.Alter: alter,
    EnumOptions.Perform: perform,
    EnumOptions.Finalize: finalize,
    EnumOptions.Report: report
}

def main():
    while True:
        option:EnumOptions = menu()
        if option == EnumOptions.Close: 
            break
        Options[option]()
       


if __name__ == "__main__":
    #print("Argumentos de inicialização passados:", sys.argv[1:])
    main()