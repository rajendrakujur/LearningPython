def check_fibonacci(n):
    if n == 0:
        return True
    elif n == 1:
        return True
    else:
        t1 = 0
        t2 = 1
        i = 3
        sum = 0
        while sum <= n:
            sum = t1 + t2
            if sum == n:
                return True
            t1 = t2
            t2 = sum
            i += 1
        return False


number = input("Enter number :")
n = (int)(number)
if check_fibonacci(n) == True:
    print(n, "is a number in Fibonacci series")
else:
    print(n, "is absent in Fibonacci series")
