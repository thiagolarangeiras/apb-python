from Options import EnumStatus, EnumReports
from database import Maintenence
import pandas as pd

def get_statusA():
    maintenances =  manutentions.query.filter_by(status=str([EnumStatus.waitingMaintenance]))
    maintenances_list = []
    
    for maintenance in maintenances:
        dict = {
            'ID': maintenance.id,
            'Nome': maintenance.name,
            'CPF': maintenance.cpf,
            'Tipo do veiculo': maintenance.type_vehicle,
            'Marca': maintenance.brand,
            'Modelo': maintenance.model,
            'Cor': maintenance.color,
            'Valor': maintenance.value,
            'Descrição': maintenance.service_description,
            'Data de entrada': maintenance.entry_date,
            'Data de saída': maintenance.departure_date,
            'Status': maintenance.status
                }
        maintenances_list.append(dict)

    df_maintenances = pd.DataFrame(maintenances_list)
    print(df_maintenances)
    