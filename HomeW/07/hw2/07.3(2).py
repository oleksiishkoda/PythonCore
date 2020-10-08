##3. Задано символьний рядок. Розробити програму, яка будує і друкує в
##алфавітному порядку множину малих, множину великих латинських  літер,
##які містяться у заданому рядку, і множину цифр, яких немає у рядку.

str1 = "Hello 2World, i'm O13k5ii."
lowercase = set()
uppercase = set()
numbers = set()

for item in range(97, 123):
    lowercase.add(chr(item))
for item in range(65, 91):
    uppercase.add(chr(item))
for item in range(48, 58):
    numbers.add(chr(item))

lower_res = set()
upper_res = set()
num_res = set()

lower_res = lowercase.intersection(str1)
upper_res = uppercase.intersection(str1)
num_res = numbers.difference(numbers.intersection(str1))

for item in sorted(lower_res):
    print(item, end = " ")
print()
for item in sorted(upper_res):
    print(item, end = " ")
print()
for item in sorted(num_res):
    print(item, end = " ")
print()
