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


def f(number, num):
    i = 2
    p = []
    l = []
    l2 = []
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

    i = 2
    p = []
    count = 0
    while i <= num:
        if primeNumber(i) == True:
            temp = num
            count = 0
            while (int)(num % i) == 0:
                count += 1
                num /= i
            l2.append(count)
            p.append(i)
        i += 1

    if len(l) < len(l2):
        small = len(l)
    else:
        small = len(l2)

    multiplier = 1
    j = 0
    while j < small:
        if l[j] < l2[j]:
            multiplier *= pow(p[j], l[j])
        else:
            multiplier *= pow(p[j], l2[j])
        j += 1
    return multiplier


number = input("Enter first number : ")
a = (int)(number)
number = input("Enter second number : ")
b = (int)(number)
print("GCD of ", a, "and", b, ":", f(a, b))
