def max(a, b, c):
    # a = (float)(a)
    # b = (float)(b)
    # c = (float)(c)
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c


a = input("Enter first number : ")
b = input("Enter second number : ")
c = input("Enter third number : ")
print("Maximum number among ", a, ",", b, "and", c, "is : ", max(a, b, c))
