##Створити змінну msg присвоїти їй значення рядка,
##який відповідає Вашому імені та прізвищу.
msg = "Oleksiy Shkoda"

##Роздрукувати вміст змінної msg двома шляхами,
##перший набравши назву змінної в інтерпретаторі,
##другий - використавши команду print().
print(msg)

##Здійснити “арифметичні” операції із рядком msg.
op1 = msg + ' Vitaliyovich'
print(op1)
op2 = msg * 3
print(op2)

##Визначити новий рядок hello. Здійснити операцію hello+msg.
##Змінити рядок hello додавши в його кінець
##символ пробілу і знову виконати операцію hello+msg.
hello = ("Hello")
print(hello + msg)
hello += " " 
print(hello + msg)

##Використовуючи зрізи та операцію поєднання змінити рядок msg до вигляду ім’я,
##по батькові, прізвище.
surname = 'Vitaliyovich'
msg = msg[0:7] + ' ' + surname + ' ' + msg[8:14]
print(msg)

##Визначити рядок s=’colorless’. Використовуючи зрізи та операцію поєднання
##змінити рядок до вигляду ‘colourless’.
s = "colorless"
s = s[0:4] + 'u' + s[4:9]
print(s)

##Використовуючи зрізи видаліть афікси у наступних словоформах:
##    dish-es, run-ning, nation-ality, un-do, pre-heat.
first = "dishes"
print(first[0:4])
second = "running"
print(second[0:3])
third = "nationality"
print(third[0:6])
fourth = "undo"
print(fourth[2:4])
fifth = "preheat"
print(fifth[3:7])
