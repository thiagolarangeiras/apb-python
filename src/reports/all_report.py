from Options import  EnumStatus,EnumReports
from database import manutentions

def get_all():
    maintenances =  manutentions.query.all()
    for maintenance in maintenances:
        print(f'{"Nome: "}{maintenance.name}\n' \
        f'{"Nº da manutenção: "}{maintenance.id}\n' \
        f'{"cpf: "}{maintenance.cpf}\n' \
        f'{"tipo do veiculo: "}{maintenance.type_vehicle}\n' \
        f'{"Marca: "}{maintenance.brand}\n' \
        f'{"Modelo: "}{maintenance.model}\n' \
        f'{"Cor: "}{maintenance.color}\n' \
        f'{"Valor: "}{maintenance.value}\n' \
        f'{"Descrição: "}{maintenance.service_description}\n' \
        f'{"Data de entrada: "}{maintenance.entry_date}\n' \
        f'{"Data de saida: "}{maintenance.departure_date}\n' \
        f'{"status: "}{maintenance.status}\n')