# 12. Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S 
# и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# s = int(input("Введите сумму чисел: "))
# p = int(input("Введите произведение чисел: "))
# x = int((-(-s) - ((-s)**2 - 4*p)**0.5) // 2)
# y = int((-(-s) + ((-s)**2 - 4*p)**0.5) // 2)
# print(f"Петя загадал {x} и {y}")


x = int(input())
y = int(input())
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)