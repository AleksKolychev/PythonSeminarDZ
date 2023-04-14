# 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input())
# m = 1
# while m < n:
#     if (m * 2 > n):
#         break
#     else:
#         m = m * 2
#         print(m)


n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1