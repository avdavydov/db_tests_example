from sqlalchemy import Column, String, INTEGER, TEXT, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Aircrafts(Base):
    __tablename__ = 'aircrafts'
    __table_args__ = {'schema': 'airline'}

    aircraft_code = Column(String(3), nullable=False, primary_key=True, comment='Код самолета, IATA')
    model = Column(TEXT, nullable=False, comment='Модель самолета')
    range = Column(INTEGER, nullable=False, comment='Максимальная дальность полета, км')


class Flights(Base):
    __tablename__ = 'flights'
    __table_args__ = {'schema': 'airline'}

    flight_id = Column(INTEGER, nullable=False, primary_key=True, comment='Идентификатор рейса')
    flight_no = Column(String(10), nullable=False, comment='Номер рейса')
    aircraft_code = Column(String(3), ForeignKey('airline.aircrafts.aircraft_code'), nullable=False, comment='Код самолета, IATA')
    status = Column(String(20), nullable=False, comment='Статус рейса')


AIRCRAFTS_ROWS = [
    {
        "aircraft_code": "773",
        "model": "Boeing 777-300",
        "range": 11100
    },
    {
        "aircraft_code": "763",
        "model": "Boeing 767-300",
        "range": 7900
    },
    {
        "aircraft_code": "SU9",
        "model": "Sukhoi Superjet-100",
        "range": 3000
    },
    {
        "aircraft_code": "320",
        "model": "Airbus A320-200",
        "range": 5700
    },
    {
        "aircraft_code": "321",
        "model": "Airbus A321-200",
        "range": 5600
    },
    {
        "aircraft_code": "319",
        "model": "Airbus A319-100",
        "range": 6700
    },
    {
        "aircraft_code": "733",
        "model": "Boeing 737-300",
        "range": 4200
    },
    {
        "aircraft_code": "CN1",
        "model": "Cessna 208 Caravan",
        "range": 1200
    },
    {
        "aircraft_code": "CR2",
        "model": "Bombardier CRJ-200",
        "range": 2700
    }
]

FLIGHTS_ROWS = [
  {
    "flight_id": 32959,
    "flight_no": "PG0550",
    "aircraft_code": "CR2",
    "status": "On Time"
  },
  {
    "flight_id": 28948,
    "flight_no": "PG0242",
    "aircraft_code": "SU9",
    "status": "Arrived"
  },
  {
    "flight_id": 33116,
    "flight_no": "PG0063",
    "aircraft_code": "CR2",
    "status": "On Time"
  },
  {
    "flight_id": 33117,
    "flight_no": "PG0063",
    "aircraft_code": "CR2",
    "status": "Arrived"
  },
  {
    "flight_id": 33111,
    "flight_no": "PG0063",
    "aircraft_code": "CR2",
    "status": "Scheduled"
  },
  {
    "flight_id": 28929,
    "flight_no": "PG0242",
    "aircraft_code": "SU9",
    "status": "Arrived"
  },
  {
    "flight_id": 33052,
    "flight_no": "PG0359",
    "aircraft_code": "CR2",
    "status": "Cancelled"
  },
  {
    "flight_id": 33043,
    "flight_no": "PG0359",
    "aircraft_code": "CR2",
    "status": "On Time"
  },
  {
    "flight_id": 33118,
    "flight_no": "PG0063",
    "aircraft_code": "CR2",
    "status": "Arrived"
  },
  {
    "flight_id": 30007,
    "flight_no": "PG0386",
    "aircraft_code": "SU9",
    "status": "Delayed"
  },
  {
    "flight_id": 28913,
    "flight_no": "PG0242",
    "aircraft_code": "SU9",
    "status": "Arrived"
  },
  {
    "flight_id": 33099,
    "flight_no": "PG0063",
    "aircraft_code": "CR2",
    "status": "Cancelled"
  },
  {
    "flight_id": 32207,
    "flight_no": "PG0425",
    "aircraft_code": "CN1",
    "status": "Departed"
  },
  {
    "flight_id": 33115,
    "flight_no": "PG0063",
    "aircraft_code": "CR2",
    "status": "Arrived"
  },
  {
    "flight_id": 33107,
    "flight_no": "PG0063",
    "aircraft_code": "CR2",
    "status": "Scheduled"
  },
  {
    "flight_id": 32806,
    "flight_no": "PG0080",
    "aircraft_code": "CN1",
    "status": "Cancelled"
  },
  {
    "flight_id": 32961,
    "flight_no": "PG0550",
    "aircraft_code": "CR2",
    "status": "Cancelled"
  },
  {
    "flight_id": 31611,
    "flight_no": "PG0494",
    "aircraft_code": "CN1",
    "status": "Delayed"
  },
  {
    "flight_id": 28895,
    "flight_no": "PG0242",
    "aircraft_code": "SU9",
    "status": "Arrived"
  },
  {
    "flight_id": 30961,
    "flight_no": "PG0004",
    "aircraft_code": "CR2",
    "status": "Delayed"
  },
  {
    "flight_id": 31946,
    "flight_no": "PG0193",
    "aircraft_code": "CN1",
    "status": "Departed"
  },
  {
    "flight_id": 28904,
    "flight_no": "PG0242",
    "aircraft_code": "SU9",
    "status": "Arrived"
  },
  {
    "flight_id": 28915,
    "flight_no": "PG0242",
    "aircraft_code": "SU9",
    "status": "Arrived"
  },
  {
    "flight_id": 33114,
    "flight_no": "PG0063",
    "aircraft_code": "CR2",
    "status": "Arrived"
  },
  {
    "flight_id": 33119,
    "flight_no": "PG0063",
    "aircraft_code": "CR2",
    "status": "Scheduled"
  },
  {
    "flight_id": 32863,
    "flight_no": "PG0080",
    "aircraft_code": "CN1",
    "status": "On Time"
  },
  {
    "flight_id": 33112,
    "flight_no": "PG0063",
    "aircraft_code": "CR2",
    "status": "Scheduled"
  },
  {
    "flight_id": 32898,
    "flight_no": "PG0147",
    "aircraft_code": "SU9",
    "status": "On Time"
  },
  {
    "flight_id": 28939,
    "flight_no": "PG0242",
    "aircraft_code": "SU9",
    "status": "Arrived"
  },
  {
    "flight_id": 33121,
    "flight_no": "PG0063",
    "aircraft_code": "CR2",
    "status": "Scheduled"
  },
  {
    "flight_id": 31363,
    "flight_no": "PG0619",
    "aircraft_code": "CN1",
    "status": "Delayed"
  },
  {
    "flight_id": 32083,
    "flight_no": "PG0708",
    "aircraft_code": "733",
    "status": "Departed"
  },
  {
    "flight_id": 28935,
    "flight_no": "PG0242",
    "aircraft_code": "SU9",
    "status": "Arrived"
  },
  {
    "flight_id": 28942,
    "flight_no": "PG0242",
    "aircraft_code": "SU9",
    "status": "Arrived"
  },
  {
    "flight_id": 31867,
    "flight_no": "PG0304",
    "aircraft_code": "SU9",
    "status": "Departed"
  },
  {
    "flight_id": 28912,
    "flight_no": "PG0242",
    "aircraft_code": "SU9",
    "status": "Arrived"
  },
  {
    "flight_id": 32871,
    "flight_no": "PG0616",
    "aircraft_code": "SU9",
    "status": "Cancelled"
  },
  {
    "flight_id": 32937,
    "flight_no": "PG0147",
    "aircraft_code": "SU9",
    "status": "Departed"
  },
  {
    "flight_id": 33120,
    "flight_no": "PG0063",
    "aircraft_code": "CR2",
    "status": "Arrived"
  },
  {
    "flight_id": 32247,
    "flight_no": "PG0604",
    "aircraft_code": "CR2",
    "status": "Delayed"
  }
]

AIRLINE_ROWS = {
    Aircrafts: AIRCRAFTS_ROWS,
    Flights: FLIGHTS_ROWS
}
