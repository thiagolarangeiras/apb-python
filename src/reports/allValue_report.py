from Options import EnumStatus, EnumReports
from database import Maintenence
import pandas as pd

def get_allValue():
    maintenances =  Maintenence.query.filter_by(status=str([EnumStatus.finished]))
    df_maintenances = pd.DataFrame(maintenances)
    df_maintenances.rename({'id': 'ID',
                            'value': 'Valor'}, axis = 1, inplace = True)
    print(df_maintenances[['ID', 'Valor']])
    print("\nTotal:{}R$\n".format(sum(df_maintenances['Valor'])))
