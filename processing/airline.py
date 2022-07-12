from db_services.db_service import get_from_postgres
from db_services.db_service import post_to_postgres

DB_NAME = 'airline'


def set_flight_status(flight_id, status) -> int:
    sql = '''
    update airline.flights
        set status = '%s'
        where flight_id = %d
    ''' % (status, flight_id)

    try:
        return post_to_postgres(sql=sql, db_name=DB_NAME)
    except Exception as e:
        raise RuntimeError(e)


def get_flight_status(flight_id) -> list:
    sql = '''
    select status
        from airline.flights
        where flight_id = %d
    ''' % flight_id

    try:
        return get_from_postgres(sql=sql, db_name=DB_NAME)
    except Exception as e:
        raise RuntimeError(e)
