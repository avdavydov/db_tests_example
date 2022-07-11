from sqlalchemy import Column, String, INTEGER, BIGINT, BOOLEAN, TEXT, ForeignKey, UniqueConstraint, \
    PrimaryKeyConstraint, NUMERIC
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Aircrafts(Base):
    __tablename__ = 'aircrafts'
    __table_args__ = {'schema': 'airline'}

    aircraft_code = Column(String(3), nullable=False, primary_key=True, comment='Код самолета, IATA')
    model = Column(TEXT, nullable=False, comment='Модель самолета')
    range = Column(INTEGER, nullable=False, comment='Максимальная дальность полета, км')


class Flights(Base):
    __tablename__ = 'aircrafts'
    __table_args__ = {'schema': 'airline'}

    flight_id = Column(INTEGER, nullable=False, primary_key=True, comment='Идентификатор рейса')
    flight_no = Column(String(10), nullable=False, comment='Номер рейса')
    aircraft_code = Column(String(3), ForeignKey('airline.aircrafts'), nullable=False, comment='Код самолета, IATA')
    status = Column(String(20), nullable=False, comment='Статус рейса')




