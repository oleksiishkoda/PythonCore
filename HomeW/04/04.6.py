##6. Для чисел, що вводяться користувачем, визначити відсоток додатних
##та від’ємних чисел. При введенні числа 0 закінчити роботу.

count = 0
dod = 0
vid = 0
num = 1
while num != 0:
	num = int(input("Enter the number: "))
	if num > 0:
		dod += 1
		count += 1
	elif num < 0:
		vid += 1
		count += 1
	else:
		break
print ("%% додатніх чисел становить - %4.2f, %% відємних становить - %4.2f"\
       %(dod/count*100, vid/count*100))
