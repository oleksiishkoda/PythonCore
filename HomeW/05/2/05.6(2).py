##6. У матриці 10x10 поміняти значення елементів у кожному рядку, розташовані
##відповідно на головній та бічній діагоналях.
from random import *
row = 10
col = 10
arr = [[0] * col for i in range(row)]
for i in range(row):
    for j in range(col):
        arr[i][j] = randint(0, 100)
        print("%4d "%arr[i][j], end = "")
    print()
print()
for i in range(row):
    temp = arr[i][i]
    arr[i][i] = arr[i][row - i - 1]
    arr[i][row - i - 1] = temp
for i in range(row):
    for j in range(col):
        print("%4d "%arr[i][j], end = "")
    print()
print()
