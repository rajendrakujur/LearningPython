############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


from art import logo
import random
from os import system, name


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
		
def draw_card():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	return random.choice(cards)

def calculate_score(score_list):
	return sum(score_list)

def compare(user_score,dealer_score):
	if user_score > 21:
		print(f"Oh no! You lost with a score {user_score} 😭")
	elif user_score == 21 and dealer_score != 21:
		print(f"Yay! You got blackjack! 😎")
	elif user_score == dealer_score:
		print(f"Oh oh! Match drawn 🤔")
	elif user_score > dealer_score:
		print(f"You won! With a total score of {user_score}.")
	else:
		print(f"You lost! With a total score of {user_score}.")


def play():
	print(logo)
	
	user = []
	dealer = []
	for _ in range(2):
		user.append(draw_card())
		dealer.append(draw_card())

	user_score = calculate_score(user)
	dealer_score = calculate_score(dealer)
	gameover = False

	while dealer_score < 17:
		dealer.append(draw_card())
		dealer_score = calculate_score(dealer)
		
	print(f"Dealer's card : {dealer[0]}.")
	print(f"Your cards : {user}")

	if user_score == 21 and dealer_score != 21:
		print(f"Yay! You got blackjack! 😎")
		gameover = True
	elif user_score > 21:
		print(f"Oh no! You lost with a score {user_score} 😭") 
		gameover = True

	while not gameover and input("'Yes' If you want to draw another card 'no' if you don't :\n").lower() == "yes":
		user.append(draw_card())
		user_score = calculate_score(user)
		if user_score > 21 and 11 in user:
			user[user.index(11)] = 1
			user_score = calculate_score(user)
		if user_score > 21:
			print(f"Oh no! You lost with a score {user_score} 😭")
			gameover = True
		print(f"Your cards : {user}")

	if not gameover and user_score + 10 < 21:
		if 1 in user:
			user[user.index(1)] = 11
			user_score = calculate_score(user)

	if not gameover:
		print(f"Your cards : {user}")
		compare(user_score,dealer_score)

play()
while input("Enter 'yes' if you want to play once more or 'no' :").lower() == "yes":
	clear()
	play()
