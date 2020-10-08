##Умова
##3. Користувач вводить число, програма повинна вивести на екран його опис.
##Наприклад, «додатне однозначне число», «від’ємне двозначне» тощо.
number = int(input("Enter the number (<1000): "))
if number > 0 and number < 1000:
    if number < 10:
        print(number, " - додатне, однозначне.")
    elif number < 100:
        print(number, " - додатне, двозначне.")
    else:
        print(number, " - додатне, тризначне.")
elif number < 0 and number > -1000:
    if number > -10:
        print(number, " - від'ємне, однозначне.")
    elif number > -100:
        print(number, " - від'ємне, двозначне.")
    else:
        print(number, " - від'ємне, тризначне.")
elif number == 0:
    print("Your number is ZERO!")
else:
    print("You entered wrong number, try again!")
    
