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


start = input("Enter Starting number :")
start = (int)(start)
last = input("Enter Last number :")
last = (int)(last)
i = start
while i < last:
    if prime(i) == True:
        print(i)
    i += 1
