import pytest

from processing.bookings import get_premium_psg_list
from .db_test import TestBases


@pytest.fixture(scope="session", autouse=True)
def test_db():
    test_base = TestBases(db_image_name='postgres:11.8')
    yield
    test_base.db.stop()


def test_get_premium_psg_list(test_db):
    assert len(get_premium_psg_list(limit=10000)) == 4


# функция, для случая если нужно оставить активным докер-контейнер после завершения работы тестов
def test_debug(test_db):
    while True:
        a = 1
    assert 1 == 2
