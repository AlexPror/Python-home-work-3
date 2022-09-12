# Задача 2. Напишите программу, которая найдёт произведение
# пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def getList():
    list = []
    for i in range(1, 10):
        list.append(i)
    return list

def multList(list):
    if len(list) % 2 == 0:
        n = 0
    else:
        n = 1
    listRes = []
    for i in range(0, len(list) // 2 + n):
        multiple = list[i] * list[len(list)-i-1]
        listRes.append(multiple)
    return listRes



print('Вычислим произведение пар чисел из списка: ')
newList = getList()
print(newList)
multiple = multList(newList)
print(f"Список произведений пар чисел списка: \n{multiple}")