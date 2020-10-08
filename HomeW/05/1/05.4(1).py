##4. Випадкові числа в діапазоні від -5 до 5 розкласти на два списки:
## в один помістити тільки додатні, у другий - тільки від’ємні.
##Числа, рівні нулю, ігнорувати.
##Вивести на екран всі згенеровані випадкові числа і елементи обох списків.
from random import *
length = int(input("Enter the length of list: "))
tempList = []
for i in range(length):
    tempList.append(randint(-5, 5))
tempList.sort()
negativeIndex = 0
positiveIndex = 0

for x in range(length):
    temp = tempList[x]
    if temp < 0:
        negativeIndex += 1
        positiveIndex += 1
    elif temp == 0:
        positiveIndex += 1
    else:
        continue     
lst1 = []
lst2 = []
for y in range(negativeIndex):
    lst1.append(tempList[y]) 
for z in range(positiveIndex, len(tempList)):
    lst2.append(tempList[z])
    
print("Generated numbers: ", tempList)
print("List 1 : ", lst1)
print("List 2 : ", lst2)



