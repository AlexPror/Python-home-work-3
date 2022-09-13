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
    sortedList = sorted(listDrob)
    maxElem = sortedList[-1]
    minElem = sortedList[0]
    result = round((maxElem - minElem), 2)
    return result

list = [1.1, 1.2, 3.1, 10.01]
listDrob = fractional_part(list)
result = find_difference(listDrob)
print(f'Разница между макс и мин знач дробной части элементов: {result}')