def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = input("Enter n value : ")
number = (int)(number)
print(number, "th fibonacci number in the series : ", fibonacci(number))
