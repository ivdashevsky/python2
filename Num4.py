# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

n = int(input("Введите число: "))
arr = []
res = 1

for i in range(-n, n+1):
    arr.append(i)

print(arr)

b = input("Введите позиции через пробел")
pos = b.split(' ')
for i in range(len(pos)):
    pos[i] = int(pos[i])

for i in range(len(pos)):
    res = res * arr[pos[i]]
    
print(res)