##2. Сформувати матрицю з чисел від 0 до 999, вивести її на екран.
##Порахувати кількість двозначних чисел в ній.
from random import *
row = int(input("Enter the number of rows: "))
col = int(input("Enter the count of columns: "))
arr = [[0] * col for x in range(row)]
count = 0
for i in range(row):
    for j in range(col):
        arr[i][j] = randint(0, 999)
        if arr[i][j] > 9 and arr[i][j] < 100:
            count += 1 
        print("%4d "%arr[i][j], end = "")
    print()
print()
print("The count of 2-digits numbers is : %d"%count)

