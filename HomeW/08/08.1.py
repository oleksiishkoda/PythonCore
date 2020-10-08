##1. Створіть словник, зв'язавши його з змінною school, і наповніть
##його даними, які б відображали кількість учнів в десяти
##різних класах (наприклад, 1а, 1б, 2б, 6а, 7в тощо.). Дізнайтеся
##скільки людей в певному класі.
##Уявіть, що в школі відбулися зміни, додайте їх в словник:
##- В трьох класах змінилося кількість учнів;
##- В школі з'явилося два нових класу;
##- В школі розформували один з класів.
##Виведіть вміст словника на екран.

school = {"1a": 23, "2c": 30, "5a": 25, "7b" : 15, "5d" : 25, \
          "9a": 28, "11a": 20, "8a": 22, "6b" : 18, "4a" : 28}
for key in school:
    print("In %2s class study %2d children." %(key, school[key]))
clas = input("Input the class: ")
if clas in school:
	 print("In %s class %d children." %(clas, school[clas]))
else:
	print("%s class is not found!" %clas)

#Зміна кількості учнів:
school['1a'] = 20
school['5a'] = 31
school['4a'] = 45

#Додавання класів до словника:
school['8b'] = 16
school['7a'] = 21

#Розформування класу:
school.pop('11a')

for key in school:
    print("In %2s class study %2d children." %(key, school[key]))
