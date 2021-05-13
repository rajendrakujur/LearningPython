def check_sign(number):
    number = (float)(number)
    if number > 0:
        print(number, "is positive")
    elif number == 0:
        print(number, "is zero")
    else:
        print(number, "is negative")


number = input("Enter number : ")
check_sign(number)
