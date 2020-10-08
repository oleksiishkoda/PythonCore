##HW_1
##1. Створити список, що містить цифри, літери алфавіту (великі та малі),
##спеціальні символи;
##2. Розділити список на декілька, кожний з яких містить тільки цифри,
##тільки літери тощо;
##3. Конвертувати списки в кортежі;
##4. Ввести з клавіатури почергово цифру, літеру чи спецсимвол і повернути
##відповідно індекс входження у відповідний кортеж;
##5. Відобразити реверс одного з кортежів.


lst = "Hell0 wor1d!$ H0w 4r3 y0u?"
lst_alpha = []
lst_num = []
lst_symb = []
for i in range(len(lst)):
    if ord(lst[i]) >= 48 and ord(lst[i]) <= 57:
        lst_num.append(lst[i]) 
    elif (ord(lst[i])>= 65 and ord(lst[i]) <= 90) or \
         (ord(lst[i])>= 97 and ord(lst[i]) <= 122):
        lst_alpha.append(lst[i])
    else:
        lst_symb.append(lst[i])
lst_alpha = tuple(lst_alpha)
lst_num = tuple(lst_num)
lst_symb = tuple(lst_symb)

print(lst)
print(lst_alpha)
print(lst_num)
print(lst_symb)

num = int(input("Enter the number to find index: "))  
alpha = input("Enter the alpha to find index: ")
symb = input("Enter the symb to find index: ")
print("Index of your number: %d" %lst_num.index(str(num))if str(num) in\
      lst_num else "Index of number is not found!")
print("Index of your alpha: %d" %lst_alpha.index(alpha)if alpha in\
      lst_alpha else "Index of alpha is not found!")
print("Index of your symbol: %d" %lst_symb.index(symb)if symb in\
      lst_symb else "Index of symbol is not found!")

print("Revrse alpha tuple: ")
for item in reversed(lst_alpha):
    print(item, end = ", ")

