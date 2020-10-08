##Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4,
##записати їх в список. Порахувати кількість додатних, від’ємних і
##нульових елементів. Вивести на екран елементи списку і пораховані кількості.
from random import *
length = 20
lst = []
zeros = 0
positive = 0
negative = 0
for i in range(length):
    lst.append(randint(-5, 4))
    print("%2d "%lst[i], end = "")
    if lst[i] < 0:
        negative += 1
    elif lst[i] > 0:
        positive += 1
    else:
        zeros += 1
print("\nNumber of zeros in the list: %d\n"\
      "Positive numbers: %d \nNegative numbers: %d"%(zeros, positive, negative))
