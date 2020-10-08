##5. Задано два символьних рядка із малих і великих латинських літер та цифр.
##Розробити програму, яка будує і друкує в алфавітному порядку множину літер,
##які є в обох масивах, і множини літер окремо першого і другого масивів.

str1 = "asdasdASFGasdGsasadaw2234325w12321"
str2 = "asdasdgfrhjFbvwbfhhjr#$@$23парц"
letters = set()
for i in range(65, 91):
    letters.add(chr(i))
for i in range(97, 123):
    letters.add(chr(i))
set_str1 = letters.intersection(str1)
set_str2 = letters.intersection(str2)
letters_in_both = set_str1.intersection(set_str2)
print("First string: ")
for item in sorted(set_str1):
    print(item, end = " ")
print()
print("Second string: ")
for item in sorted(set_str2):
    print(item, end = " ")
print()
print("Letters in both strings: ")
for item in sorted(letters_in_both):
    print(item, end = " ")
print()
