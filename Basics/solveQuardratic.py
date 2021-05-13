def solveQuardratic(a, b, c):
    print("solution for quardratic equation :", end=" ")
    if a >= 0:
        print("+", a, "x2", end=" ")
    else:
        print("-", a, "x2", end=" ")
    if b >= 0:
        print("+", b, "x", end=" ")
    else:
        print("-", b, "x", end=" ")
    if c >= 0:
        print("+", c)
    else:
        print("-", c)
    D = (b ** 2) - (4 * a * c)
    if D == 0:
        print("The Equation is having same real roots")
    elif D > 0:
        print("The Equation is having real and distinct roots")
    else:
        print(
            "The Equation is having imaginary roots which are conjugate to each other"
        )

    x1 = ((-1) * b + ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
    x2 = ((-1) * b - ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
    print("is X1 : ", x1, "and X2 : ", x2)


number = input("Enter square term's coefficient : ")
a = (float)(number)
number = input("Enter linear term's coefficient : ")
b = (float)(number)
number = input("Enter constant Term : ")
c = (float)(number)
solveQuardratic(a, b, c)
