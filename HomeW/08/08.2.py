##Створіть словник, ключами є слова, а значеннями – список слів-синонімів
##до нього. Програма отримує на вхід кількість слів N. Далі користувач
##вводить слова-ключі та відповідні йому синоніми. 
##Передбачити: 
##1) на запит (слово) користувача вивести список синонімів;
##2) користувач вводить речення, в якому є слова (ключі, що містяться в словнику).
##Замінити їх синонімами та вивести речення на екран.

from random import randint
synonims = {"beautiful": ["pretty", "charming"], \
           "warm": ["hot", "friendly"], \
           "kind": ["good", "well"], "magic": ["fairy", "imaginary"],\
           "nice": ["pleasant", "fine"], "modest":["descreet"]}
word = input("Input a word: ")
if word in synonims.keys():
    print("For %s are synonims: " %word)
    print(synonims[word])
else:
    print("There is not such a word in dictionary!")
sent = input("Input a sentence: ")
for key in synonims:
    if sent.find(key) >= 0:
        syn_list = synonims[key]
        new_sent = sent.replace(key, syn_list[randint(0, \
                                                 len(synonims[key]) - 1)])
print(new_sent)

##Проблема даного алгоритму в тому, що він зберігає лише перше замінене
##слово в речені, якщо в речені більше одного слова, які потрібно замінити,
##воно не буде працювати, адже стрінг зберігся вперший раз і вже не може
##змінитися. Я пізніше викладу оновлений документ, де буде виправлено це.
