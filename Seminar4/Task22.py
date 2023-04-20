# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n=(int(input("Введите число элементов: ")))
list_1=[]
for i in range(n):
    elm = int(input("Введите элемент "))
    list_1.append(elm)
print(list_1)

m=(int(input("Введите число элементов: ")))
list_2 = []
for i in range(m):
    elm = int(input("Введите элемент "))
    list_2.append(elm)
print(list_2)

c = list(set(list_1) & set(list_2))
print(c)

# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
# set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
# set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
# print(i, end=' ')