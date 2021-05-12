def cube(n):
    temp = (int)(n)
    sum = 0

    while temp != 0:
        digit = (int)(temp % 10)
        sum += digit * digit * digit
        temp = (int)(temp / 10)

    if (int)(n) == (int)(sum):
        return True
    else:
        return False


testcases = input("Enter number of testcases :")
t = (int)(testcases)
while t > 0:
    number = input("Enter number : ")
    if cube(number) == True:
        print(number, "is an Armstrong Number.")
    else:
        print(number, "is not an Armstrong number")
    t = t - 1
