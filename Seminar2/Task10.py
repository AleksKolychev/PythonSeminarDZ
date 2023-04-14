# 10. На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


# print("Введите количество монет: ")
# n = int(input())
# k = 0
# print("Как лежат монеты? ")
# for i in range(n):
#     v = int(input())
#     if v == 1:
#         k += 1
# if k < n / 2:
#     print(f"Нужно перевертуть {k} монет")
# else:
#     print(f"Нужно перевертуть {n - k} монет")


n = int(input())
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input())
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)