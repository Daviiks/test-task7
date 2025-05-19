from math import factorial as fct

def my_factorial(number):
    if number < 0:
            raise ValueError("Факториал определен только для неотрицательных чисел")
    return fct(number)

def get_factorial_from_input():
    user_input = input('Введите число для факториала: ')
    try:
        number = int(user_input)
        return my_factorial(number)
    except ValueError as e:
        if "неотрицательных" in str(e):
            raise ValueError(e)
        else:
            raise ValueError('Введите целое число')