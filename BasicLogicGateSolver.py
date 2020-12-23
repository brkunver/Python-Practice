# Written By Burakhan Unver | 23.12.2020

# This program solves 6 basic logic gate output for given 2 inputs
# At least one input must be 1 or 0 otherwise gives error


# returns True if user want to end the program, otherwise false
def continue_program():
	while True:
		choice = input("\nWant to continue ? \n 'y' for yes \n 'n' for no \n Choice : ").lower()
		if choice == "y":
			print("\n")
			return True
		elif choice == "n":
			print("\n")
			return False
		else:
			print("Error, please enter an valid choice")


# -----Gate Functions-----


# returns the users input, for wrong input it shows an error
def gate_input():
	while True:
		print("Enter an input : 1 or 0 or x")
		x = input("Your input : ")
		if x == "1" or x == "0" or x == "x":
			return x
		else:
			print("Input error, please enter an valid input")


# and gate solver function
def and_gate():
	input1 = gate_input()
	input2 = gate_input()

	if input1 == "x" and input2 == "x":
		print("Error, At least one variable have to be 1 or 0")
		and_gate()
	elif input1 == "1" and input2 == "1":
		print("Answer is One")
	elif (input1 == "x" and input2 == "1") or (input1 == "1" and input2 == "x"):
		print("Answer is X")
	else:
		print("Answer is Zero")


# or gate solver function
def or_gate():
	input1 = gate_input()
	input2 = gate_input()

	if input1 == "x" and input2 == "x":
		print("Error, At least one variable have to be 1 or 0")
		or_gate()
	elif input1 == "1" or input2 == "1":
		print("Answer is One")
	elif (input1 == "x" and input2 == "0") or (input1 == "0" and input2 == "x"):
		print("Answer is X")
	else:
		print("Answer is Zero")


# nand gate solver function
def nand_gate():
	input1 = gate_input()
	input2 = gate_input()

	if input1 == "x" and input2 == "x":
		print("Error, At least one variable have to be 1 or 0")
		nand_gate()
	elif input1 == "0" or input2 == "0":
		print("Answer is One")
	elif (input1 == "x" and input2 == "1") or (input1 == "1" and input2 == "x"):
		print("Answer is X'")
	else:
		print("Answer is Zero")


# nor gate solver function
def nor_gate():
	input1 = gate_input()
	input2 = gate_input()

	if input1 == "x" and input2 == "x":
		print("Error, At least one variable have to be 1 or 0")
		nor_gate()
	elif input1 == "1" or input2 == "1":
		print("Answer is Zero")
	elif (input1 == "x" and input2 == "0") or (input1 == "0" and input2 == "x"):
		print("Answer is X'")
	else:
		print("Answer is One")


# xor gate solver function
def xor_gate():
	input1 = gate_input()
	input2 = gate_input()

	if input1 == "x" and input2 == "x":
		print("Error, At least one variable have to be 1 or 0")
		xor_gate()
	elif input1 == input2:
		print("Answer is Zero")
	elif (input1 == "x" and input2 == "0") or (input1 == "0" and input2 == "x"):
		print("Answer is X")
	elif (input1 == "x" and input2 == "1") or (input1 == "1" and input2 == "x"):
		print("Answer is X' ")
	else:
		print("Answer is One")


# xnor gate solver function
def xnor_gate():
	input1 = gate_input()
	input2 = gate_input()

	if input1 == "x" and input2 == "x":
		print("Error, At least one variable have to be 1 or 0")
		xnor_gate()
	elif input1 == input2:
		print("Answer is One")
	elif (input1 == "x" and input2 == "0") or (input1 == "0" and input2 == "x"):
		print("Answer is X'")
	elif (input1 == "x" and input2 == "1") or (input1 == "1" and input2 == "x"):
		print("Answer is X")
	else:
		print("Answer is Zero")


# this variable controls the loop
cont = True

# program loop, starts with True
while cont:
	print("Please Select a gate \n", "Gates Are : 'and','or','nand','nor','xor','xnor'")

	# turning choice string to lowercase for prevent mistakes
	gate_choice = input("Selection = ").lower()

	# test cases for choice
	if gate_choice == "and":
		and_gate()

	elif gate_choice == "or":
		or_gate()

	elif gate_choice == "nand":
		nand_gate()

	elif gate_choice == "nor":
		nor_gate()

	elif gate_choice == "xor":
		xor_gate()

	elif gate_choice == "xnor":
		xnor_gate()

	else:
		print("Please enter a valid gate name")
		continue

	# checking if user wants to proceed
	cont = continue_program()
