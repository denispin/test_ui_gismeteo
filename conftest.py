import pytest

from application import Application
from helpers.asserts_accumulator import AssertsAccumulator


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


@pytest.fixture(scope='session')
def asserts():
    """
    Initialize asserts accumulator.
    :return: Asserts accumulator object.
    """

    asserts_accumulator = AssertsAccumulator()
    return asserts_accumulator
