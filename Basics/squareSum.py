def squareSum(n):
    result = 0
    for i in range(n + 1):
        result += i * i
    return result


number = input("Enter number :")
n = (int)(number)
print("Square sum of first ", n, "natural numbers : ", squareSum(n))
