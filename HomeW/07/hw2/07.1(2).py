##1. Задано n рядочків символів.  Розробити програму, яка визначає і друкує
##окремо приголосні та голосні малі літери латинського алфавіту, які є в
##кожному рядку.

row = int(input("Enter the number of rows: "))
lst1 = [0] * row
for i in range(row):
    lst1[i] = input("Enter the %d row of symbols: " %(i+1))
set1 = set()
for item in range(97, 123):
    set1.add(chr(item))

set_vow = {'a', 'e', 'y', 'u', 'o', 'i'}
set_con = set1 - set_vow
set_vow_res = set()
set_con_res = set()

for item in (lst1[0]):
    if item in set_vow: set_vow_res.add(item)
    if item in set_con: set_con_res.add(item)
    
i = 1
for i in range(row):
    set_vow_res = set_vow_res.intersection(lst1[i])
    set_con_res = set_con_res.intersection(lst1[i])


print("Repetitive vowels:")
for item in set_vow_res:
    print(item, end = " ")
print()
print("Repetitive consonants:")
for item in set_con_res:
    print(item, end = " ")
print()

