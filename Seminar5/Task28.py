# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

a = int(input("Первое число: "))
b = int(input("Второе число: "))
def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)
print(f"Сумма: {sum(a, b)}")