from sqlalchemy import Column, String, INTEGER, BIGINT, BOOLEAN, TEXT, ForeignKey, UniqueConstraint, \
    PrimaryKeyConstraint, NUMERIC
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Ticket(Base):
    __tablename__ = 'tickets'
    __table_args__ = {'schema': 'bookings'}

    ticket_id = Column(BIGINT, nullable=False, unique=True, autoincrement=True, primary_key=True, comment='Номер билета')
    passenger_id = Column(String(20), nullable=False, comment='Идентификатор пассажира')
    passenger_name = Column(TEXT, nullable=False, comment='Имя пассажира')


class Ticket_Flights(Base):
    __tablename__ = 'ticket_flights'
    __table_args__ = {'schema': 'bookings'}

    ticket_id = Column(BIGINT, ForeignKey('bookings.tickets'), nullable=False, unique=True,  comment='Номер билета')
    flight_id = Column(INTEGER, nullable=False, comment='Идентификатор рейса')
    amount = Column(NUMERIC(10, 2), nullable=False, comment='Стоимость перелета')
    PrimaryKeyConstraint(ticket_id, flight_id)


class Boarding_Passes(Base):
    __tablename__ = 'boarding_passes'
    __table_args__ = {'schema': 'bookings'}

    boarding_no = Column(BIGINT, nullable=False, unique=True, autoincrement=True, primary_key=True, comment='Номер посадочного талона')
    ticket_id = Column(BIGINT, ForeignKey('bookings.tickets'), nullable=False, unique=True, comment='Номер билета')
    seat_no = Column(String(4), nullable=False, comment='Номер места')






