##2. Задано чотирицифрове натуральне число. 
##    a) Знайти добуток цифр цього числа.
##    b) Записати число в реверсному порядку.
number = int(input("Введіть чотирицифрове число: "))
if number > 999 and number < 10000:
    rez = int(str(number)[0]) * int(str(number)[1]) * int(str(number)[2]) *\
          int(str(number)[3])
    revers = int(str(number)[-1] + str(number)[-2] + str(number)[-3] +\
                 str(number)[-4])
    print("Добуток цифр числа %d становить %d \nРеверс числа %d, : %d"\
          %(number, rez, number, revers))
    
    
else:
    print("Error, try again!")
