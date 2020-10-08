# 3. Вивести на екран таблицю множення (від 1 до 9).
x = 1
while x < 10:
    for y in range(1,10):
        
        print("%2d * %d = %2d"%(y, x, y * x),end = "   ")
    x += 1
    print("\n")
