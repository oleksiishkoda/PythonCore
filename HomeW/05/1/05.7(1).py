##7. У списку знайти елементи, які в ньому зустрічаються тільки один раз,
##і вивести їх на екран.
from random import *
length = int(input("Enter the length of list: "))
lst = []
unique = []
for i in range(length):
    lst.append(randint(0, 10))
    print("%2d "%lst[i], end = "")
print()
for x in range(length):
    if lst.count(lst[x]) == 1:
        unique.append(lst[x])
print("\nUniqual numbers in list:")
for y in range(len(unique)):
    print("%2d "%unique[y], end = "")
print()
