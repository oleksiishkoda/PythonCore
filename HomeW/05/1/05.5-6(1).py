##5. Заповнити список випадковими додатними і від’ємними цілими числами.
##Вивести його на екран. Видалити з списку всі від’ємні елементи і знову вивести.
from random import *
length = int(input("Enter the length of list: "))
lst = []
for i in range(length):
    lst.append(randint(-100, 100))
print("Generated numbers: ")
for j in range(length):
    print("%d "%lst[j], end = "")
print()
x = 0
while x < len(lst):
    if lst[x] < 0:
        lst.remove(lst[x])
    else:
        x += 1
print("\nList without negative numbers: ")
for y in range(len(lst)):
    print("%d "%lst[y], end = "")
print()
    
##6. У другому списку зберегти індекси парних елементів першого списку.
##Наприклад, якщо дано список зі значеннями 8, 3, 15, 6, 4, 2, то
##другий треба заповнити значеннями 1, 4, 5, 6 (або 0, 3, 4, 5 - якщо
##індексація починається з нуля), оскільки саме в цих позиціях першого
##масиву стоять парні числа.
lst2 = []
for z in range(len(lst)):
    if lst[z] % 2 == 0:
        lst2.append(z)
print("\nIndexes: ")
for g in range(len(lst2)):
    print("%d "%lst2[g], end = "")
