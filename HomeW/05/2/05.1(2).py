##1. Порахувати суми кожного рядка і кожного стовпця матриці.
##Доповнити її стовпцем, який містить суми елементів рядків та рядком,
##елементами якого є суми елементів стовпців.
from random import *
row = int(input("Enter the count of rows: "))
col = int(input("Enter the count of columns: "))
lst = [[0] * col for i in range(row)]
for i in range(row):
    for j in range(col):
        lst[i][j] = randint(0, 100)
        print("%4d "%lst[i][j], end = "")
    print()
print()

for i in range(row):
    lst[i].append(sum(lst[i]))
    
lst_sum_col = []
for j in range(col + 1):
    sumCol = 0
    for i in range(row):
       sumCol += lst[i][j]
    lst_sum_col.append(sumCol)
lst.append(lst_sum_col)

for i in range(row + 1):
    for j in range(col + 1):
        print("%5d "%lst[i][j], end = "")
    print()
print()
