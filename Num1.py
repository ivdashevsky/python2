# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = input("Введите число: ")

arr = list(n)
res = 0
for i in range(len(arr)):
    if arr[i].isdigit() == True:
        res += int(arr[i])
print(res)