# Задача 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементов 3 и 9, ответ: 12

def sum_elem_index(*args):
    sum = 0
    for i in range(0, len(list)):
        if i % 2 != 0:
            sum = list[i] + sum
    return sum
list = [2, 3, 5, 9, 3]
result = sum_elem_index(list)
print(result)