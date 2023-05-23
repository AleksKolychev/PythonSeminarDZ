# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# Вывод: [1, 9, 13, 14, 19]

# from random import randint
 
# lo, hi = 3, 8
# data = [randint(1, 10) for _ in range(20)]
# print("Начальный массив:", data, sep='\n')
# indexes = [i for i, v in enumerate(data) if lo <= v <= hi]
# print("Индексы:", indexes, sep='\n')


list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input())
max_number = int(input())
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i)