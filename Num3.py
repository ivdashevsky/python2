# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

k = int(input("Введите число: "))
arr = []
elem = 0
res = 0

for i in range(k):
    elem = round((1 + 1/(i+1))**(i+1),2)
    arr.append(elem)

for i in range(len(arr)):
    res = res + arr[i]

print(arr)
print(round(res,2))