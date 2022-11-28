from Options import  EnumStatus,EnumReports
from reports.menu_report import menu_reports
from reports.all_report import get_all
from reports.statusA_report import get_statusA
from reports.statusM_report import get_statusM
from reports.statusC_report import get_statusC
from reports.statusF_report import get_statusF
from reports.allValue_report import get_allValue
from reports.people_report import get_people


Options = {
    EnumReports.AllReportsMaintenance: get_all, 
    EnumReports.ReportsMaintenanceA: get_statusA,
    EnumReports.ReportsMaintenanceM: get_statusM,
    EnumReports.ReportsMaintenanceC: get_statusC,
    EnumReports.ReportsMaintenanceF: get_statusF,
    EnumReports.TotalValueRepots: get_allValue,
    EnumReports.PeopleReports: get_people
}



def report():
    while True:
        option:EnumReports = menu_reports()
        if option == EnumReports.CloseReports: 
            break
        Options[option]()
    
   
    





    
    
   