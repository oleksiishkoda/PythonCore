##Умова:
##У програмі генерується випадкове ціле число від 0 до 100.
##Користувач повинен його відгадати не більше ніж за 10 спроб.
##Після кожної невдалої спроби повинно повідомлятися чи більше
##чи менше введене користувачем число, ніж те, що загадане.
##Якщо за 10 спроб число не відгадане, то вивести загадане число.

from random import *
num = randint(1, 100)
count = 1
while count <= 10:
    numTry = int(input("Try to guess the number, (press '0' to exit): "))
    if numTry == 0:
        break
    elif numTry > num:
        print("\nGo down! That's your %d try, you have %d attempts left!"\
              %(count, 10 - count))
        count += 1
    elif numTry < num:
        print("\nGo up! That's your %d try, you have %d attempts left!"\
              %(count, 10 - count))
        count += 1
    else:
        print("You win!")
        break
else:
    print("You lost. That's a right number: %d" %num)
    
print("Good game!")
