#Calculator

from art import logo
from os import system, name

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def add(n1,n2):
	return n1+n2

def subtract(n1,n2):
	return n1-n2

def multiply(n1,n2):
	print("multiply called")
	return n1*n2

def divide(n1,n2):
	return  n1/n2

def Calculator():
	operation = {"+":add,"-":subtract,"*":multiply,"/":divide}
	num1 = float(input("Enter First number : "))

	should_continue = True
	while should_continue:
		for symbol in operation:
			print(f"{symbol}")

		operation_symbol = input("Enter operation symbol : ")

		num2 = float(input("Enter Second number : "))

		answer = operation[operation_symbol](num1,num2)
		print(f"{num1} {operation_symbol} {num2} = {answer}")

		if input("Enter y for continue calculation or n to start a new Calculator:") == "y":
			num1 = answer
		else:
			should_continue = False
			clear()
			print(logo)
			Calculator()

print(logo)
Calculator()
