##У змінній записаний текст. Словом вважається послідовність непорожніх символів,
##які йдуть підряд, слова розділені одним або більше пробілом.
##Програмно створіть словник, в якому ключами є слова з речення,
##а значеннями – кількість входження в речення.


str1 = "Hello world!:*"" The weather is hello beautiful, the world 3 is beautiful."
print(str1)
dictionary = {}
set_alpha = set()
for i in range(65, 91):
	set_alpha.add(chr(i))
for i in range(97, 123):
	set_alpha.add(chr(i))
temp_list = []
new_list = []
for i in range(len(str1)):
	if str1[i] in set_alpha:
		temp_list.append(str1[i].lower())
	elif len(temp_list) > 0:
		new_list.append("".join(temp_list))
		temp_list.clear()
	else: pass
for item in new_list:
	if item in dictionary: pass
	else:
		dictionary[item] = new_list.count(item)
		
for key in dictionary:
        print('%10s: %d'%(key, dictionary[key]))
        
        

