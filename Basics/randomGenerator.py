import random


def random_generator(start, last):
    start = (int)(start)
    last = (int)(last)
    return random.randint(start, last + 1)


start = input("Enter starting number :")
last = input("Enter last number :")
print(
    "Random number generated in the range of ",
    start,
    "and",
    last,
    ":",
    random_generator(start, last),
)
