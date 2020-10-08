##8. У списку випадкових цілих чисел поміняти місцями
##мінімальний і максимальний елементи.
from random import *
length = int(input("Enter the length of list: "))
lst1 = []
for i in range(length):
    lst1.append(randint(-100, 100))
    print("%2d "%lst1[i], end = "")
print()
minElem = min(lst1)
maxElem = max(lst1)
print("Min : %d\nMax : %d" %(minElem, maxElem))

minElemIndex = lst1.index(minElem)
maxElemIndex = lst1.index(maxElem)

temp = lst1[minElemIndex]
lst1[minElemIndex] = lst1[maxElemIndex]
lst1[maxElemIndex]= temp

for j in range(length):
    print("%2d "%lst1[j], end = "")
print()
