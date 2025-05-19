import pytest, unittest
from factorial import *

def main():
    """Основная функция программы."""
    print("Программа вычисления факториала")
    while True:
        try:
            result = get_factorial_from_input()
            print("Результат:", result)
            break  # Выход из цикла, если успешно
        except ValueError as e:
            print("Ошибка:", e)
            print("Попробуйте ещё раз!")
        except TypeError as e:
            print("Ошибка типа:", e)
            print("Попробуйте ещё раз!")

def run_unittests():
    print("Запуск unittest тестов...")
    loader = unittest.TestLoader()
    suite = loader.discover('Tests', pattern='test_library_unittest.py')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()

def run_pytests():
    print("\nЗапуск pytest тестов...")
    return pytest.main(["-v", "Tests/test_factorial_pytest.py"]) == 0

if __name__ == '__main__':
    main()
    unittest_success = run_unittests()
    pytest_success = run_pytests()
    

