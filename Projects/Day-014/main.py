import random
from os import name, system
from game_data import data
from art import logo


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def play():
    print(logo)

    random_1 = random.randint(0, len(data))
    score = 0
    gameover = False
    winner = random_1
    while not gameover:
        
        random_2 = random.randint(0, len(data))
        while random_2 == random_1:
            random_2 = random.randint(0, len(data))

        choice = input((f"Who has more follower A: {data[random_1]['name']} or B: {data[random_2]['name']}\n")        )
        print(f"A:{data[random_1]['name']} has {data[random_1]['follower_count']} follower")
        print(f"B:{data[random_2]['name']} has {data[random_2]['follower_count']} follower")

        if choice.lower() == "a":
            if data[random_1]["follower_count"] > data[random_2]["follower_count"]:
                winner = random_1
                score += 1
            else:
                gameover = True
        elif choice.lower() == "b":
            if data[random_1]["follower_count"] < data[random_2]["follower_count"]:
                score += 1
                winner = random_2
            else:
                gameover = True

        random_1 = winner
    print(f"You lost the game with {score} score.")


play()
while input("'yes' if you want to play once more or 'no'\n").lower() == "yes":
    clear()
    play()
