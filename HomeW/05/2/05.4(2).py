##4. Знайти максимальний елемент серед мінімальних елементів стовпців матриці.
from random import *
row = int(input("Enter the count of rows: "))
col = int(input("Enter the count of columns: "))
arr = [[0] * col for i in range(row)]
for i in range(row):
    for j in range(col):
        arr[i][j] = randint(0, 100)
        print("%4d "%arr[i][j], end = "")
    print()
print()

lst_min_elem = []
for j in range(col):
    temp_min = arr[i][j]
    for i in range(row):
        if temp_min > arr[i][j]:
            temp_min = arr[i][j]
    lst_min_elem.append(temp_min)
print("Min elems of every column:\n", lst_min_elem)
print("\nMax elem of min elems is : %d"%max(lst_min_elem))
