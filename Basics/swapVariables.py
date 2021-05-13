def swap_variables(a, b):
    b = a


a = input("Enter first number :")
b = input("Enter second number :")
print("Numbers before swapping a :", id(a), "b :", id(b))
swap_variables(a, b)
print("Numbers after swapping a :", a, "b :", b)
