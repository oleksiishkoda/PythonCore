##7. Змінити послідовність стовпців матриці так, щоб елементи її
##першого рядка були відсортовані за зростанням.
from random import *
row = int(input("Enter the count of rows: "))
col = int(input("Enter the count of columns: "))
arr = [[0] * col for i in range(row)]
print("Generated list: ")
for i in range(row):
    for j in range(col):
        arr[i][j] = randint(0, 100)
        print("%4d "%arr[i][j], end = "")
    print()
print()
lst_copy = [[0] * col for i in range(row)]
for i in range(row):
    for j in range(col):
        lst_copy[i][j] = arr[i][j]
arr[0].sort()

for i in range(col):
    x = 0
    while x < col:
        if arr[0][i] == lst_copy[0][x]:
            for z in range(1, row):
                for y in range(col):
                    if lst_copy[z][x] == arr[z][y]:
                        temp = arr[z][y]
                        arr[z][y] = arr[z][i]
                        arr[z][i] = temp
        x += 1

print("Result: ")
for i in range(row):
    for j in range(col):
        print("%4d "%arr[i][j], end = "")
    print()
print()

##Довго мучився із цим завданням, думаю можна його зробити простіше, однак я,
##мабуть, черговий раз заплутався і не зміг знайти простішого розв'язку.
