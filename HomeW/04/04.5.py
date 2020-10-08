##5. Дано число P  і число H. Користувач вводить послідовність чисел.
##Визначити: суму тих чисел, які менше P; добуток чисел, які більші за H;
##кількість чисел, що знаходяться  в діапазоні значень від P до H.
##При введенні числа рівного P або H, припинити обчислення та вивести результат.

p = int(input("Enter P (P < H): "))
h = int(input("Enter H (P < H): "))
if p >= h:
        print("Error!")
else:
        suma = 0
        dob = 1
        count = 0
        num = int(input("Enter the number: "))
        while num != p and num != h:
                if num < p:
                        suma += num
                elif num > h:
                        dob *= num
                else:
                        count += 1
                num = int(input("Enter the number: "))
        else:
                if num == p:
                        print("Ви ввели число рівне P і закінчили програму.")
                else:
                        print("Ви ввели число рівне H і закінчили програму.")
        print("Suma = %d, Dob = %d, Count = %d"%(suma, dob, count))
