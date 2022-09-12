# Задача 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 10.01] => 0.19
# 1. Задать список вещественных чисел
# 2. Выделить дробную часть у элементов
# 3. Найти макс и мин значение дробной части.
# 4. Найти разницу между макс и мин знач.
import math

def fractional_part(*args):
    listDrob = []
    for i in range(len(list)):
        listDrob.append(round(list[i] % 1, 2))
    return listDrob

def find_difference(listDrob):
    max_float = 0
    min_float = 0
    for i in range(len(listDrob)):
        if listDrob[i] > max_float:
            max_float = listDrob[i]
        elif listDrob[i] < max_float:
            min_float = listDrob[i]
    result = max_float - min_float
    return result

list = [1.1, 1.2, 3.1, 10.01]
fractions = fractional_part(list)
result = find_difference(fractions)
print(f'Разница между макс и мин знач дробной части элементов: {result}')