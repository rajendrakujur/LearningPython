def prime(number):
    n = (int)(number)
    if n == 2:
        return True
    if (int)(n % 2) == 0:
        return False
    i = 3
    while i < n:
        if (int)(n % i) == 0:
            return False
        i += 2
    return True


number = input("Enter number :")
if prime(number) == True:
    print(number, "is prime")
else:
    print(number, "is not prime")
