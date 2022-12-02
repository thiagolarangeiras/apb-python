from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,Numeric,DateTime,Float
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('sqlite:///apb.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))
db = declarative_base()
db.query = db_session.query_property()


class Maintenence(db):
    __tablename__ = 'maintenence'
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