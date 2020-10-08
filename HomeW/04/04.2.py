## Вводяться десять натуральних чисел більше 2.
##Порахувати, скільки серед них чисел, що кратні 5-ти.
count = 1
rez = 0
while count <= 10:
    number = int(input("Enter the %d number ( > 2 ): " %count))
    if number % 5 == 0:
        rez += 1
    count += 1
print("Your result is: %d numbers." %rez)
