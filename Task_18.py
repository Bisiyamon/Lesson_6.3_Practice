""" Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X """

import random

N = int(input("Введите количество элементов в массиве: "))
A = random.sample(range(1, 2*N), N)
print(A)

X = int(input("Введите число: "))
diff = 2*N
possition = 0

for i in range(N):
    if abs(A[i]-X) <= diff:
        diff = abs(A[i]-X)
        find_number = A[i]
        possition = i

print(f"Ближайшее число {find_number} находится на позиции {possition}")


