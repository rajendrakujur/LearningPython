def cubeSum(n):
    result = 0
    for i in range(n + 1):
        result += i * i * i
    return result


number = input("Enter number :")
n = (int)(number)
print("Cube sum of first ", n, "natural numbers : ", cubeSum(n))
