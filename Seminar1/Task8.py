# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку 
# на два прямоугольника). 

n = int(input("Введите размер 1: "))
m = int(input("Введите размер 2: "))
k = int(input("Сколько долек отломить? "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Получится')
else:
    print('Не получится')