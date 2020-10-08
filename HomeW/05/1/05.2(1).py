##Заповнити список дійсними числами введенням з клавіатури.
##Порахувати суму і добуток елементів списку.
##Вивести на екран сам список, отримані суму і добуток його елементів.
length = int(input("Enter the lenght of list: "))
lst = []
suma = 0
dob = 1
for i in range(length):
    lst.append(int(input("Enter the number in list: ")))
    dob *=lst[i] 
suma = sum(lst)
print("\nList:")
for j in range(length):
    print("%d "%lst[j], end = "")
print("\nSum of elements: %d \nDobutok = %d" %(suma,dob ))
