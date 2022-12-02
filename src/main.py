#!python
from Options import EnumOptions

from menu import menu
from models.maintenance import register 
from models.pf_maintenance import perform
from models.fl_maintenance import finalize
from maintenance.update import update
from reports.report import report

Options = {
    EnumOptions.Register: register, 
    EnumOptions.Update: update,
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
    main()