from Options import EnumStatus, EnumReports
from database import Maintenence
import pandas as pd

def get_allValue():
    maintenances =  Maintenence.query.filter_by(status=str([EnumStatus.finished]))
    maintenances_list = []
    for maintenance in maintenances:
        dict = {
            'ID': maintenance.id,
            'Valor': maintenance.value
                }
        maintenances_list.append(dict)
    
    if len(maintenances_list) <= 0:
        print(f"Nenhuma Manutenção encontrada")
        return
    
    df_maintenances = pd.DataFrame(maintenances_list)

    print(df_maintenances)
    print("\nTotal:{}R$\n".format(sum(df_maintenances['Valor'])))
