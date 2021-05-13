def multiplicationTable(number):
    for i in range(1, 11):
        print(number, "x", i, " : ", number * i)


number = input("Enter number : ")
number = (int)(number)
print("Multiplication Table for ", number)
multiplicationTable(number)
