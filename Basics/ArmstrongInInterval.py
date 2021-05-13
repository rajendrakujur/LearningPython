def checkArmstrong(number):
    temp = number
    sum = 0
    # print("checking for", number)
    while temp > 0:
        temp2 = (int)(temp % 10)
        sum += temp2 ** 3
        temp /= 10
    if sum == number:
        return True
    else:
        return False


def ArmstrongInInterval(start, end):
    for i in range(start, end + 1):
        if checkArmstrong(i) == True:
            print(i)


number = input("Enter starting number : ")
start = (int)(number)
number = input("Enter last number : ")
last = (int)(number)
print("Armstrong number in the range of ", start, "to", last, "are as follows :")
ArmstrongInInterval(start, last)
