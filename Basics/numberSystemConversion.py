def special_char(number):
    if number == 10:
        return "A"
    elif number == 11:
        return "B"
    elif number == 12:
        return "C"
    elif number == 13:
        return "D"
    elif number == 14:
        return "E"
    elif number == 15:
        return "F"


def conversion(number):
    number = (int)(number)
    decimal = (int)(number)
    temp = decimal
    binary = []
    while temp >= 1:
        binary.append((str)((int)(temp % 2)))
        temp /= 2
    binary.reverse()
    print("binary format of ", number, " is : ", "".join(binary))

    temp = decimal
    octal = []
    while temp >= 1:
        octal.append((str)((int)(temp % 8)))
        temp /= 8
    octal.reverse()
    print("octal format of ", number, " is : ", "".join(octal))

    temp = decimal
    hex = []
    while temp >= 1:
        t = (int)(temp % 16)
        if t <= 9:
            hex.append((str)(t))
        else:
            hex.append(special_char(t))
        temp /= 16
    hex.reverse()
    print("hexadecimal format of ", number, " is : ", "".join(hex))


number = input("Enter number in decimal format :")
conversion(number)
