from Options import EnumStatus, EnumReports
from database import Maintenence
import pandas as pd

def get_allValue():
    maintenances =  Maintenence.query.filter_by(status=str([EnumStatus.finished]))
    df_maintenances = pd.DataFrame(maintenances)
    df_allValue['ID'] = df_maintenances['id']
    df_allValue['Valor'] = df_maintenances['value']
    print(df_allValue)
    print("\nTotal:{}R$\n".format(sum(df_allValue['Valor'])))
