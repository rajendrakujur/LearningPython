from replit import clear
from art import logo

should_continue = True
dictionary = {}
while should_continue :
	clear()
	print(logo)
	name = input("What is your name?\n")
	amount = int(input("What is your bid?: $"))
	dictionary[name] = amount
	choice = input("Want to continue? yes or no\n")
	if choice == "no":
		should_continue = False

def find_winner(dictionary):
	maximum_amount = 0
	for temp_name in dictionary:
		if dictionary[temp_name] > 	maximum_amount:
			maximum_amount = dictionary[temp_name]
			winner = temp_name
			
	print(f"{winner} has won and will pay ${dictionary[winner]}.")

find_winner(dictionary)
