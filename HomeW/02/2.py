##Умова
##2. Залежно від вибору користувача, обчислити площу або
##прямокутника, або трикутника, або круга.
##Якщо обрані прямокутник або трикутник,
##то треба запросити довжини сторін; круга – його радіус.
choice = int(input("The area of wich figure you want to calculate?\n \
                   1. Rectangle\n \
                   2. Triangle \n \
                   3. Circle\n"))
from math import *
if choice == 1:
    a = int(input("Enter the length of first side: "))
    b = int(input("Enter the length of second side: "))
    square = a * b
    print("The square of rectangle is ", square)
elif choice == 2:
    a = int(input("Enter the length of base: "))
    b = int(input("Enter the height: "))
    square = 1 / 2 * a * b
    print("The square of triangle is ", square)
elif choice == 3:
    a = int(input("Enter the radius: "))
    square = pi * a ** 2 
    print("The square of rectangle is ", square)
else:
    print("Wrong choice!\nError!")
