def powerOfTwo(number):
    for i in range(number + 1):
        # print("2^", i, 2 ** i)
        print("2^", i, pow(2, i))


number = input("Enter max limit : ")
number = (int)(number)
print("Powers of two till ", number)
powerOfTwo(number)
