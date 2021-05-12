def fibonacci_number(number):
    n = (int)(number)
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        t1 = 0
        t2 = 1
        i = 3
        result = 0
        while i <= n:
            result = t1 + t2
            t1 = t2
            t2 = result
            i += 1
    return result


number = input("Enter number :")
print(number, "th fibonacci number :", fibonacci_number(number))
