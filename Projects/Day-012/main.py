#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include three different difficulty levels (e.g., 10 guesses in easy mode,7 guesses in medium mode, only 5 guesses in hard mode).

from art import logo
import random
from os import system, name


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
	

def play():
	print(logo)
	print("I am picking a number between 1 to 100")
	generated_number = random.randint(0,100)
	level = input("Enter the difficulty level to play: hard or medium or easy\n")
	if level.lower() == "hard":
		remaining_attempts = 5
	elif level.lower() == "medium":
		remaining_attempts = 7
	elif level.lower() == "easy":
		remaining_attempts = 10

	gameover = False
	while remaining_attempts and not gameover:
		guessed_number = int(input("Guess a number\n"))
		if guessed_number == generated_number:
			print("Bingo you guessed it right!!")
			gameover = True
		elif guessed_number >= 0.8 * generated_number and guessed_number < generated_number:
			print("That's pretty closer(but low)")
		elif guessed_number <= 0.8 * generated_number :
			print("That's too low.")
		elif guessed_number > generated_number and guessed_number <= 1.2* generated_number:
			print("That's pretty close(but high)")
		else:
			print("That's too high")

	if remaining_attempts == 0:
		print("Sad to see you lose")

play()
while input("Enter yes if you want to play again or no\n").lower() == "yes":
	clear()
	play()
