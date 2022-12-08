from Options import EnumStatus, EnumReports
from database import Maintenence
import pandas as pd

def get_statusM():
    maintenances =  Maintenence.query.filter_by(status=str([EnumStatus.onMaintenance]))
    df_maintenances = pd.DataFrame(maintenances)
    df_maintenances.rename({'id': 'ID',
                            'name': 'Nome',
                            'cpf': 'CPF',
                            'type_vehicle': 'Tipo do veiculo',
                            'brand': 'Marca',
                            'model': 'Modelo',
                            'color': 'Cor',
                            'value': 'Valor',
                            'service_description': 'Descrição',
                            'entry_date': 'Data de entrada',
                            'departure_date': 'Data de saída',
                            'status': 'Status'}, axis = 1, inplace = True)
    print(df_maintenances)