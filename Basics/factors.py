def primeNumber(number):
    if number == 2:
        return True
    if (int)(number % 2) == 0:
        return False
    else:
        i = 3
        while i < number:
            if (int)(number % i) == 0:
                return False
            i += 1
        return True


def factors(number):
    i = 2
    l = []
    p = []
    count = 0
    while i <= number:
        if primeNumber(i) == True:
            temp = number
            count = 0
            while (int)(number % i) == 0:
                count += 1
                number /= i
            l.append(count)
            p.append(i)
        i += 1
    print(p)
    print(l)


number = input("Enter number : ")
number = (int)(number)
factors(number)
