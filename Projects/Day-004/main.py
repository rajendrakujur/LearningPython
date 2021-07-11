import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = int(input("What do you choose 0 for rock,  for paper or 2 for sciessors"))

if choice == 0:
	print(f"You have choosen\n{rock}")
elif choice == 1:
	print(f"You jave chhosen\n{paper}")
elif choice == 2:
	print(f"You have choosen\n{scissors}")

computer_choice = random.randint(0,2)

if computer_choice == 0:
	print(f"Computer has choosen\n{rock}")
elif computer_choice == 1:
	print(f"Computer has chhosen\n{paper}")
else:
	print(f"Computer has choosen\n{scissors}")

if choice >= 3:
	print("Invalid Choice, You lose!")
elif choice == 0 and computer_choice == 2:
	print("You won!")
elif computer_choice == 0 and choice == 2:
	print("You lose!")
elif choice > computer_choice:
	print("You won!")
elif choice == computer_choice:
	print("It's a draw!")
