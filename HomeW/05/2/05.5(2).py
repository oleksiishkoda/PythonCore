##5. Дві матриці заповнюються введенням з клавіатури. В елементи третьої матриці
##такої ж розмірності записати більші з відповідних елементів перших двох.
row = int(input("Enter the count of rows: "))
col = int(input("Enter the count of columns: "))
lst1 = [[0] * col for i in range(row)]
##lst2 = list(lst1)     Чомусь таким способом після ініціалізації список 1
##                        вбирає в себе значення списку 2, хоча id у них різні, я перевіряв
lst2 = [[0] * col for i in range(row)]
for i in range(row):
    for j in range(col):
        lst1[i][j] = int(input("Enter the number in first list: "))
    print()
print()
for i in range(row):
    for j in range(col):
        lst2[i][j] = int(input("Enter the number in second list: "))
    print()
print()

print("List 1:\n", lst1)
print("List 2:\n", lst2)

lst3 = [[0] * col for i in range(row)]
print("List 3:")
for i in range(row):
    for j in range(col):
        if lst1[i][j] >= lst2[i][j]:
            lst3[i][j] = lst1[i][j]
        else:
            lst3[i][j] = lst2[i][j]
        print("%2d "%lst3[i][j], end = "")
    print()
print()
