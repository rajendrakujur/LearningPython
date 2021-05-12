def find_area(radius):
    pi = (float)(22 / 7)
    area = pi * (int)(radius) * (int)(radius)
    print("Area of the circle with radius : ", radius, "is : ", area, "square units.")


r = input("Enter radius : ")
radius = (int)(r)
find_area(radius)
