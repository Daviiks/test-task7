import pytest
import random
from src.factorial import *

@pytest.mark.parametrize(
    "input_number, expected_result",
    [
        (5, 120),    # input_number=5 → expected_result=120
        (0, 1),      # input_number=0 → expected_result=1
        (1, 1),      # input_number=1 → expected_result=1
    ], ids='str'
)

# Тест 1: Проверка корректного вычисления факториала
def test_my_factorial_positive(input_number, expected_result):
    assert my_factorial(input_number) == expected_result, \
        f"Факториал {input_number} должен быть {expected_result}, но получено"

# Позитивные тесты
@pytest.mark.parametrize(
    "number, expected",
    [
        (0, 1),
        (5, 120),
    ],
    ids=["0! = 1", "5! = 120"]
)
def test_factorial_success(number, expected):
    assert my_factorial(number) == expected

# Негативные тесты
@pytest.mark.parametrize(
    "invalid_input, error_type",
    [
        (-2, ValueError),
        ("abc", TypeError),
    ],
    ids=["Отрицательное число", "Строка вместо числа"]
)
def test_factorial_errors(invalid_input, error_type):
    with pytest.raises(error_type):
        my_factorial(invalid_input)

@pytest.fixture
def random_number():
    # Фикстура, возвращающая случайное число от 1 до 100.
    return random.randint(1, 100)

def test_random_number_in_range(random_number):
    assert 1 <= random_number <= 100, \
        f"Число {random_number} вне диапазона [1, 100]"

def test_factorial_with_random_number(random_number):
    result = my_factorial(random_number)
    print(f"Проверка факториала для {random_number}: {result}")
    assert result > 0 
