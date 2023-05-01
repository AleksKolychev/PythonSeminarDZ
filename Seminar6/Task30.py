# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5

# Вывод: 7 9 11 13 15


array = []
a1 = int(input('Ввести первый элемент: '))
d = int(input('Введите разность: '))
n = int(input('Введите количество элементов: '))
for i in range(1, n + 1):
    array.append(a1 + d * (i - 1))
print(array)