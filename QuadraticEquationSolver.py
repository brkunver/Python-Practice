# Written by Burakhan Unver 23.12.2020


def continue_check():
	while True:
		inp = input("Do you want to continue? y for yes, n for no\n")
		if inp == "y":
			return True
		elif inp == "n":
			return False
		else:
			print("Error, please enter 'y' or 'n'")


cont = True
while cont:
	print("Please enter coefficients of equation for ax^2+bx+c = 0")
	try:
		a = int(input("a = "))
		b = int(input("b = "))
		c = int(input("c = "))
	except ValueError:
		print("Error, please enter valid numbers")
		continue

	delta = b ** 2 - 4 * a * c
	print("Delta is ", delta)
	if delta < 0:
		print("There is no real roots")
	else:
		x1 = (-b + delta ** 0.5) / (2 * a)
		x2 = (-b - delta ** 0.5) / (2 * a)
		if delta == 0:
			print("There is one real root")
			print("x = ", x1)
		else:
			print("There are two real roots")
			print("x1 = %.5f  " % x1, "\nx2 = %.5f" % x2)
	cont = continue_check()
