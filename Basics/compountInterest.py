def compoud_interest(p, r, t):
    print("Principal Amount : ", p, "INR")
    print("Rate of Interest : ", r, "%")
    print("Time Duration :", t, "years")

    interest = (float)(p) * pow((1 + (float)(r) / 100), (int)(t))
    print("Compound interest :", interest)


p = input("Enter Principal amount :")
r = input("Enter rate of Interest :")
t = input("Enter time duration : ")
compoud_interest(p, r, t)
