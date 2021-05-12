number = input("Enter number : ")
number = int(number)
result = 1
count = 1
while count <= number:
    result *= count
    count += 1
print("Factorial of ", number, " : ", result)
