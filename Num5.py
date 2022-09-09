# Реализуйте алгоритм перемешивания списка

import random

# вариант 1

print("Вариант 1: рандомный индекс")
lst = list(range(5))
print("Изначальный список: ", lst)

for i in range(len(lst)):
    index_new = random.randint(0,len(lst)-1)
    temp = lst[i]
    lst[i] = lst[index_new]
    lst[index_new] = temp
print("Перемешанный список", lst, "\n")

# вариант 2

print("Вариант 2: (shuffle)")
lst = list(range(1, 10, 2))
print("Изначальный список: ", lst)

random.shuffle(lst)
print("Перемешанный список", lst)
