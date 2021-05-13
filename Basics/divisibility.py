def divisibility(divisor, dividend):
    if (int)(dividend % divisor) == 0:
        return True
    else:
        return False


number = input("Enter dividend : ")
dividend = (int)(number)
number = input("Enter divisor : ")
divisor = (int)(number)
if divisibility(divisor, dividend) == True:
    print("Divisible")
else:
    print("Not Divisible")
