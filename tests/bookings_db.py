from sqlalchemy import Column, String, INTEGER, BIGINT, TEXT, ForeignKey, PrimaryKeyConstraint, NUMERIC
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Ticket(Base):
    __tablename__ = 'tickets'
    __table_args__ = {'schema': 'bookings'}

    ticket_id = Column(BIGINT, nullable=False, unique=True, autoincrement=True, primary_key=True,
                       comment='Номер билета')
    passenger_id = Column(String(20), nullable=False, comment='Идентификатор пассажира')
    passenger_name = Column(TEXT, nullable=False, comment='Имя пассажира')


class Ticket_Flights(Base):
    __tablename__ = 'ticket_flights'
    __table_args__ = {'schema': 'bookings'}

    ticket_id = Column(BIGINT, ForeignKey('bookings.tickets.ticket_id'), nullable=False, unique=True, comment='Номер билета')
    flight_id = Column(INTEGER, nullable=False, comment='Идентификатор рейса')
    amount = Column(NUMERIC(10, 2), nullable=False, comment='Стоимость перелета')
    PrimaryKeyConstraint(ticket_id, flight_id)


class Boarding_Passes(Base):
    __tablename__ = 'boarding_passes'
    __table_args__ = {'schema': 'bookings'}

    boarding_no = Column(BIGINT, nullable=False, unique=True, autoincrement=True, primary_key=True,
                         comment='Номер посадочного талона')
    ticket_id = Column(BIGINT, ForeignKey('bookings.tickets.ticket_id'), nullable=False, unique=True, comment='Номер билета')
    seat_no = Column(String(4), nullable=False, comment='Номер места')


TICKET_ROWS = [
    {
        "ticket_id": 5432000987,
        "passenger_id": "8149 604011",
        "passenger_name": "VALERIY TIKHONOV"
    },
    {
        "ticket_id": 5432000988,
        "passenger_id": "8499 420203",
        "passenger_name": "EVGENIYA ALEKSEEVA"
    },
    {
        "ticket_id": 5432000989,
        "passenger_id": "1011 752484",
        "passenger_name": "ARTUR GERASIMOV"
    },
    {
        "ticket_id": 5432000990,
        "passenger_id": "4849 400049",
        "passenger_name": "ALINA VOLKOVA"
    },
    {
        "ticket_id": 5432000991,
        "passenger_id": "6615 976589",
        "passenger_name": "MAKSIM ZHUKOV"
    },
    {
        "ticket_id": 5432000992,
        "passenger_id": "2021 652719",
        "passenger_name": "NIKOLAY EGOROV"
    },
    {
        "ticket_id": 5432000993,
        "passenger_id": "0817 363231",
        "passenger_name": "TATYANA KUZNECOVA"
    },
    {
        "ticket_id": 5432000994,
        "passenger_id": "2883 989356",
        "passenger_name": "IRINA ANTONOVA"
    },
    {
        "ticket_id": 5432000995,
        "passenger_id": "3097 995546",
        "passenger_name": "VALENTINA KUZNECOVA"
    },
    {
        "ticket_id": 5432000996,
        "passenger_id": "6866 920231",
        "passenger_name": "POLINA ZHURAVLEVA"
    },
    {
        "ticket_id": 5432000997,
        "passenger_id": "6030 369450",
        "passenger_name": "ALEKSANDR TIKHONOV"
    },
    {
        "ticket_id": 5432000998,
        "passenger_id": "8675 588663",
        "passenger_name": "ILYA POPOV"
    },
    {
        "ticket_id": 5432000999,
        "passenger_id": "0764 728785",
        "passenger_name": "ALEKSANDR KUZNECOV"
    },
    {
        "ticket_id": 5432001000,
        "passenger_id": "8954 972101",
        "passenger_name": "VSEVOLOD BORISOV"
    },
    {
        "ticket_id": 5432001001,
        "passenger_id": "6772 748756",
        "passenger_name": "NATALYA ROMANOVA"
    },
    {
        "ticket_id": 5432001002,
        "passenger_id": "7364 216524",
        "passenger_name": "ANTON BONDARENKO"
    },
    {
        "ticket_id": 5432001003,
        "passenger_id": "3635 182357",
        "passenger_name": "VALENTINA NIKITINA"
    },
    {
        "ticket_id": 5432001004,
        "passenger_id": "8252 507584",
        "passenger_name": "ALLA TARASOVA"
    },
    {
        "ticket_id": 5432001005,
        "passenger_id": "1026 982766",
        "passenger_name": "OKSANA MOROZOVA"
    },
    {
        "ticket_id": 5432001006,
        "passenger_id": "7107 950192",
        "passenger_name": "GENNADIY GERASIMOV"
    },
    {
        "ticket_id": 5432001007,
        "passenger_id": "4765 014996",
        "passenger_name": "RAISA KONOVALOVA"
    }
]

TICKET_FLIGHTS_ROWS = [
    {
        "ticket_id": 5432000987,
        "flight_id": 28935,
        "amount": 6200.00
    },
    {
        "ticket_id": 5432000988,
        "flight_id": 28935,
        "amount": 6200.00
    },
    {
        "ticket_id": 5432000990,
        "flight_id": 28939,
        "amount": 18500.00
    },
    {
        "ticket_id": 5432000989,
        "flight_id": 28939,
        "amount": 6200.00
    },
    {
        "ticket_id": 5432000991,
        "flight_id": 28913,
        "amount": 18500.00
    },
    {
        "ticket_id": 5432000992,
        "flight_id": 28913,
        "amount": 6200.00
    },
    {
        "ticket_id": 5432000993,
        "flight_id": 28913,
        "amount": 6200.00
    },
    {
        "ticket_id": 5432000994,
        "flight_id": 28912,
        "amount": 6800.00
    },
    {
        "ticket_id": 5432000995,
        "flight_id": 28912,
        "amount": 6200.00
    },
    {
        "ticket_id": 5432000996,
        "flight_id": 28929,
        "amount": 6200.00
    },
    {
        "ticket_id": 5432000998,
        "flight_id": 28904,
        "amount": 18500.00
    },
    {
        "ticket_id": 5432000999,
        "flight_id": 28904,
        "amount": 6200.00
    },
    {
        "ticket_id": 5432000997,
        "flight_id": 28904,
        "amount": 6200.00
    },
    {
        "ticket_id": 5432001001,
        "flight_id": 28895,
        "amount": 6200.00
    },
    {
        "ticket_id": 5432001000,
        "flight_id": 28895,
        "amount": 6200.00
    },
    {
        "ticket_id": 5432001002,
        "flight_id": 28895,
        "amount": 6200.00
    },
    {
        "ticket_id": 5432001003,
        "flight_id": 28948,
        "amount": 18500.00
    },
    {
        "ticket_id": 5432001004,
        "flight_id": 28948,
        "amount": 6800.00
    },
    {
        "ticket_id": 5432001005,
        "flight_id": 28942,
        "amount": 6200.00
    },
    {
        "ticket_id": 5432001007,
        "flight_id": 28915,
        "amount": 6200.00
    },
    {
        "ticket_id": 5432001006,
        "flight_id": 28915,
        "amount": 6200.00
    }
]

BOARDING_PASSES_ROWS = [
    {
        "boarding_no": 5432000959,
        "ticket_id": 5432000997,
        "seat_no": "19F"
    },
    {
        "boarding_no": 5432000962,
        "ticket_id": 5432000989,
        "seat_no": "18E"
    },
    {
        "boarding_no": 5432000963,
        "ticket_id": 5432001005,
        "seat_no": "17C"
    },
    {
        "boarding_no": 5432000965,
        "ticket_id": 5432001006,
        "seat_no": "16C"
    },
    {
        "boarding_no": 5432000969,
        "ticket_id": 5432000995,
        "seat_no": "17A"
    },
    {
        "boarding_no": 5432000970,
        "ticket_id": 5432000993,
        "seat_no": "19E"
    },
    {
        "boarding_no": 5432000974,
        "ticket_id": 5432000988,
        "seat_no": "10E"
    },
    {
        "boarding_no": 5432000977,
        "ticket_id": 5432000987,
        "seat_no": "7A"
    },
    {
        "boarding_no": 5432000978,
        "ticket_id": 5432001002,
        "seat_no": "12C"
    },
    {
        "boarding_no": 5432000979,
        "ticket_id": 5432001000,
        "seat_no": "11D"
    },
    {
        "boarding_no": 5432000981,
        "ticket_id": 5432001001,
        "seat_no": "11A"
    },
    {
        "boarding_no": 5432000982,
        "ticket_id": 5432001007,
        "seat_no": "8D"
    },
    {
        "boarding_no": 5432000983,
        "ticket_id": 5432000999,
        "seat_no": "8F"
    },
    {
        "boarding_no": 5432000984,
        "ticket_id": 5432000996,
        "seat_no": "14A"
    },
    {
        "boarding_no": 5432000986,
        "ticket_id": 5432000994,
        "seat_no": "6F"
    },
    {
        "boarding_no": 5432000987,
        "ticket_id": 5432000992,
        "seat_no": "5F"
    },
    {
        "boarding_no": 5432000988,
        "ticket_id": 5432000990,
        "seat_no": "3F"
    },
    {
        "boarding_no": 5432000989,
        "ticket_id": 5432001004,
        "seat_no": "6F"
    },
    {
        "boarding_no": 5432000990,
        "ticket_id": 5432000991,
        "seat_no": "1D"
    },
    {
        "boarding_no": 5432000996,
        "ticket_id": 5432000998,
        "seat_no": "2C"
    },
    {
        "boarding_no": 5432001000,
        "ticket_id": 5432001003,
        "seat_no": "2C"
    }
]

BOOKINGS_ROWS = {
    Ticket: TICKET_ROWS,
    Ticket_Flights: TICKET_FLIGHTS_ROWS,
    Boarding_Passes: BOARDING_PASSES_ROWS
}
