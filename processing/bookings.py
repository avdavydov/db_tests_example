from db_services.db_service import get_from_postgres

DB_NAME = 'bookings'

# Получить список пассажиров, траты которых более limit
def get_premium_psg_list(limit) -> list:
    sql = '''
            select passenger_name, sum(amount)
                    from bookings.tickets
                             join bookings.ticket_flights using (ticket_id)
                    group by 1
                    having sum(amount) > %d ''' % limit

    try:
        return get_from_postgres(sql=sql, db_name=DB_NAME)
    except Exception as e:
        raise RuntimeError(e)
