def sum(number):
    sum = 0
    number = (int)(number)
    for i in range(1, number + 1):
        sum += i
    return sum


number = input("Enter last number : ")
print("Sum of first", number, "natural numbers : ", sum(number))
