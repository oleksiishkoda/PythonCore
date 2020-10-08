##Умова
##5. Відома грошова сума. Розміняти її купюрами 200, 100, 10 і монетою 1 грн.,
##якщо це можливо.
suma = int(input("Enter the sum: "))
newsuma = suma
if newsuma // 200 > 0:
    coop200 = newsuma // 200
    newsuma -= coop200 * 200
    if newsuma // 100 > 0:
        coop100 = newsuma // 100
        newsuma -= coop100 * 100
        if newsuma // 10 > 0:
            coop10 = newsuma // 10
            newsuma -= coop10 * 10
            monets = newsuma
            if monets > 0:
                print("Суму ", suma, " грн. розміняли ", coop200,\
                  " купюрами по 200 грн., ", coop100, " купюрами по 100 грн.,",\
                  coop10, " купюрами по 10 грн. і ", monets, " монетами.")
            else:
                print("Суму ", suma, " грн. розміняли ", coop200,\
                  " купюрами по 200 грн., ", coop100, " купюрами по 100 грн.,",\
                  coop10, " купюрами по 10 грн. ")
                
        else:
            monets = newsuma
            if monets > 0:
                print("Суму ", suma, " грн. розміняли ", coop200,\
                  " купюрами по 200 грн., ", coop100, " купюрами по 100 грн.,",\
                  " і ", monets, " монетами.")
            else:
                 print("Суму ", suma, " грн. розміняли ", coop200,\
                  " купюрами по 200 грн., ", coop100, " купюрами по 100 грн.")
    else:
        if newsuma // 10 > 0:
            coop10 = newsuma // 10
            newsuma -= coop10 * 10
            monets = newsuma
            if monets > 0:
                print("Суму ", suma, " грн. розміняли ", coop200,\
                  " купюрами по 200 грн., ", coop10, " купюрами по 10 грн. і ",\
                      monets, " монетами.")
            else:
                print("Суму ", suma, " грн. розміняли ", coop200,\
                  " купюрами по 200 грн., ", coop10, " купюрами по 10 грн. ")
                
        else:
            monets = newsuma
            if monets > 0:
                print("Суму ", suma, " грн. розміняли ", coop200,\
                  " купюрами по 200 грн. і ", monets, " монетами.")
            else:
                 print("Суму ", suma, " грн. розміняли ", coop200,\
                  " купюрами по 200 грн.")
elif newsuma // 100 > 0:
        coop100 = newsuma // 100
        newsuma -= coop100 * 100
        if newsuma // 10 > 0:
            coop10 = newsuma // 10
            newsuma -= coop10 * 10
            monets = newsuma
            if monets > 0:
                print("Суму ", suma, " грн. розміняли ",coop100,\
                      " купюрами по 100 грн.,",\
                  coop10, " купюрами по 10 грн. і ", monets, " монетами.")
            else:
                print("Суму ", suma, " грн. розміняли ", coop100,\
                      " купюрами по 100 грн.,",\
                  coop10, " купюрами по 10 грн. ")
                
        else:
            monets = newsuma
            if monets > 0:
                print("Суму ", suma, " грн. розміняли ", coop100,\
                      " купюрами по 100 грн. і ", monets, " монетами.")
            else:
                 print("Суму ", suma, " грн. розміняли ", coop100,\
                       " купюрами по 100 грн.")
elif newsuma // 10 > 0:
    coop10 = newsuma // 10
    newsuma -= coop10 * 10
    monets = newsuma
    if monets > 0:
        print("Суму ", suma, " грн. розміняли ", coop10,\
                      " купюрами по 10 грн. і ", monets, " монетами.")
    else:
        print("Суму ", suma, " грн. розміняли ",\
                      coop10, " купюрами по 10 грн. ")
elif newsuma > 0:
    print("Суму ", suma, " грн. розміняли ", newsuma, " монетами.")
elif newsuma == 0:
    print("Ви ввели 0.")
else:
    print("Error! Ty again!")

