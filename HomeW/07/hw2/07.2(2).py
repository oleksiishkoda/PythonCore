##2. Задано символьний рядок. Розробити програму, яка вилучає з цього рядка всі
##повторні входження цифр і знаків арифметичних операцій.

str1 = "He110 w0++rd! %%546500Yeyeye"
print("Start: \n%s" %str1)
numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
symbols = {'+', '-', '*', '/', '%'}
new_lst = []
for item in str1:
    if item in new_lst and (item in numbers or item in symbols):
        continue
    else:
        new_lst.append(item)
new_str = ''.join(new_lst)
print("Result: \n%s"%new_str)
