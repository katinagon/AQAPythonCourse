import pytest


@pytest.fixture()
def fixture_for_all_tests():
    print("Делаем что-то до теста")
    yield
    print("Делаем что-то после теста")
