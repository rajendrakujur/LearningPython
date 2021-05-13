def area_of_Triangle(l, b, h):
    if l == b and b == h:
        area = ((l * l) * 3 ** 2) / 4
    else:
        perimeter = (l + b + h) / 2
        area = (
            perimeter
            * ((perimeter * (perimeter - l) * (perimeter - b) * (perimeter - h)) ** 0.5)
            / 2
        )
    return area


length = input("Enter Length :")
length = (int)(length)
height = input("Enter height : ")
height = (int)(height)
breadth = input("Enter Breadth : ")
breadth = (int)(breadth)
print("Area of Triangle :", area_of_Triangle(length, breadth, height), "square units")
