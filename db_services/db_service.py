from .engine_factory import EngineFactory
engine = EngineFactory()

def get_from_postgres(sql, db_name, schema_name=None) -> list:
    result = []
    pg_engine = engine.get_engine(db_name=db_name, schema_name=schema_name)
    try:
        with pg_engine.connect() as connection:
            cursor = connection.execution_options(stream_result=True).execute(sql)
            for row in cursor:
                result.append(list(row))
    except Exception as e:
        raise RuntimeError(f'Ошибка при обращении к БД: {e}')
    return result


def post_to_postgres(sql, db_name, schema_name=None) -> int:
    pg_engine = engine.get_engine(db_name=db_name, schema_name=schema_name)
    rows_processed = 0
    try:
        with pg_engine.connect() as connection:
            cursor = connection.execution_options(stream_result=True, isolation_level='AUTOCOMMIT').execute(sql)
            rows_processed = cursor.rowcount
            cursor.close()
    except Exception as e:
        raise RuntimeError(f'Ошибка при выполнении операции {sql} в БД: {e}')
    return rows_processed
