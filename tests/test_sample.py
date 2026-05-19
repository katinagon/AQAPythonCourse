import pytest


@pytest.fixture(scope="module")
def scope_module():
    print("Выполнится один раз на файл")


@pytest.fixture(autouse=True)
def autouse_fix():
    print("Выполняется для каждого теста")


def test1(scope_module):
    print("Тест 1")


@pytest.mark.xfail
def test2(scope_module):
    print("Тест 2")


@pytest.mark.skip
def test3(scope_module):
    print("Тест 3")


@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (2, 2, 4),
        (5, 5, 10),
        (-1, 1, 0),
    ],
)
@pytest.mark.smoke
def test_sum(num1, num2, expected):
    assert num1 + num2 == expected
