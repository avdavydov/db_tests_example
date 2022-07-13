import pytest

from processing.airline import set_flight_status, get_flight_status
from processing.bookings import get_premium_psg_list
from .db_test import TestBases


@pytest.fixture(scope="session", autouse=True)
def test_db():
    # Этот блок будет выполнен перед запуском тестов
    test_base = TestBases(db_image_name='postgres:11.8')
    yield
    # Этот блок будет выполнен после окончания работы тестов
    test_base.db.stop()


# Тест метода processing.bookings.get_premium_psg_list()
# В текущих тестовых данных, для limit=10000, корректный результат == 4
def test_get_premium_psg_list(test_db):
    assert len(get_premium_psg_list(limit=10000)) == 4


# Тест метода processing.airline.get_flight_status()
# Для flight_id=33043 корректный результат 'On Time'
def test_get_flight_status_before(test_db):
    assert get_flight_status(flight_id=33043) == [['On Time']]


# Тест метода processing.airline.set_flight_status()
# В таблице airline.flights только одна запись с flight_id=33043, поэтому корректный результат - 1
# !!!Тест меняет состояние тестовой среды!!!
def test_set_flight_status(test_db):
    assert set_flight_status(flight_id=33043, status='Delayed') == 1


# Тест метода processing.airline.get_flight_status()
# После выполнения теста test_set_flight_status(test_db) состояние тестовой среды изменилось.
# Корректный результат теста для flight_id=33043 - 'Delayed'
def test_get_flight_status_after(test_db):
    assert get_flight_status(flight_id=33043) == [['Delayed']]


# тест, для случая если нужно оставить активным докер-контейнер после завершения работы тестов
def test_debug(test_db):
    while True:
        pass
