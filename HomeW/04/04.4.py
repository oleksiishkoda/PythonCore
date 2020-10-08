##4. Вивести на екран «прямокутник», утворений з двох видів символів.
##Контур прямокутника повинен складатися з одного символу, а "заливка" - з іншого.

char1 = str(input("Enter the contour: "))
char2 = str(input("Enter the filling: "))
length = int(input("Enter the length of rectangle: "))
height = int(input("Enter the height of rectangle: "))
for x in range(1, height + 1):
	for y in range(1, length + 1):
		if x == 1 or x == height:
			print(char1, " ", end = "")
		else:
			if y == 1 or y == length:
				print(char1, " ", end = "")
			else:
				print(char2, " ", end = "")
	print("\n")
