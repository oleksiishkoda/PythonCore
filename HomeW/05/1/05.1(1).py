##1. Заповнити один список випадковими числами, інший - введеними з клавіатури
##числами, в третій записати суми відповідних елементів перших двох.
##Вивести вміст списків на екран.
first = int(input("Enter the length of first list: "))
second = int(input("Enter the length of second list: "))
from random import *
lst1= [0] * first
lst1 = [randint(1, 100) for i in range(first)]
lst2 = [0] * second
lst2 = [int(input("Enter the number: "))for j in range(second)]	
print("List 1: \n", lst1)
print("List 2: \n", lst2)
if len(lst1) >= len(lst2):
	suma = [0] * first
	lst2.extend([0] * (len(lst1) - len(lst2)))
else:
	suma = [0] * second
	lst1.extend([0] * (len(lst2) - len(lst1)))
suma = [lst1[g] + lst2[g] for g in range(len(suma))]
print("Sum : \n", suma)
