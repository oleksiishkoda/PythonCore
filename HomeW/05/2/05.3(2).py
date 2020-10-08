##3. Матриця 5x4 заповнюється введенням з клавіатури (крім останніх
##елементів рядків). Програма повинна обчислювати суму введених елементів
##кожного рядка і записувати її в останній рядок. Наприкінці слід вивести
##отриману матрицю.
row = 5
col = 4
arr = [[0] * col for i in range(row)]
for i in range(row):
    suma = 0
    for j in range(col):
        if j == col - 1:
            arr[i][j] = suma
        else:
            arr[i][j] = int(input("Enter the number: "))
            suma += arr[i][j]
print()
for i in range(row):
    for j in range(col):
        print("%2d "%arr[i][j], end = "")
    print()
print()
