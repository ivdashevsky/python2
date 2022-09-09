# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input("Введите число "))
arr = []

for i in range(1,n+1):
    arr.append(i)
print(arr)

for i in range(1,len(arr)):
    arr[i] = arr[i-1] * (i+1)
print(arr)