from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,Numeric,DateTime,Float
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from Options import EnumStatus

engine = create_engine('sqlite:///manutention.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))
db = declarative_base()
db.query = db_session.query_property()


class manutentions(db):
    __tablename__ = 'manutention'
    id = Column(Integer, primary_key=True)
    name = Column(String(), index=True)
    cpf = Column(String())
    type_vehicle = Column(String())
    brand = Column(String())
    model = Column(String())
    color = Column(String())
    value = Column(Float())
    service_description = Column(String())
    entry_date  = Column(DateTime, default=datetime.now)
    departure_date  = Column(DateTime, default=datetime.min)
    status  = Column(String())

    def __repr__(self):
        return f'{"Nome: "}{self.name}\n' \
               f'{"Nº da manutenção: "}{self.id}\n' \
               f'{"cpf: "}{self.cpf}\n' \
               f'{"tipo do veiculo: "}{self.type_vehicle}\n' \
               f'{"Marca: "}{self.brand}\n' \
               f'{"Modelo: "}{self.model}\n' \
               f'{"Cor: "}{self.color}\n' \
               f'{"Valor: "}{self.value}\n' \
               f'{"Descrição: "}{self.service_description}\n' \
               f'{"Data de entrada: "}{self.entry_date}\n' \
               f'{"Data de saida: "}{self.departure_date}\n' \
               f'{"status: "}{self.status}'
               
                

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    db.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()