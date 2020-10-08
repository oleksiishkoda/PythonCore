##4. Задано символьний рядок. Розробити програму, яка знаходить групи цифр,
##записаних підряд, і вилучає із них всі початкові нулі, крім останнього,
##якщо за ним знаходиться крапка. Друкує модифікований масив по сорок символів
##у рядку.
str1 = "Hello000.sfsdf00"
lst1 = []
numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
for i in range(len(str1)):
    if str1[i] == '0':
        j = i
        while str1[j] == '0' or str1[j] != len(str1) - 1:
            j += 1
        if str1[i - 1] == '.':
            for k in range(j + 1):
                lst1.append(str1[k])
        elif str1[j] == '.':
            lst1.append('0')
            i = j - 1
        else:
            lst1.append(str1[j])
    else:
        lst1.append(str1[i])
    
print(lst1)
