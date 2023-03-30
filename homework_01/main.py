"""
Домашнее задание №1
Функции и структуры данных
"""
import math

def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i ** 2 for i in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    if number == 0 or number == 1:
        return False
    i = 2
    prime = True
    while i <= math.sqrt(number) and prime is True:
        if number % i == 0:
            prime = False
        i += 1
    if prime:
        return True
    else:
        return False

def filter_numbers(number_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return [i for i in number_list if i % 2 != 0]

    elif filter_type == EVEN:
        return [i for i in number_list if i % 2 == 0]

    elif filter_type == PRIME:
        return list(filter(is_prime, number_list))



