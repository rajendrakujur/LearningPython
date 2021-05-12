# print("Enter Principal amount :")
# p = input()
# print("Enter rate Yealy in percentage : ")
# r = input()
# print("Enter duration : ")
# t = input()
# interest = (int)(p) * (float)(r) * (int)(t) / 100
# print("Interest for the given data will be :", interest)

# Simple Interest Method
def simple_interest(p, r, t):
    print("Principal Amount : ", p)
    print("Rate of interest : ", r)
    print("Time Duration : ", t)

    interest = (int)(p) * (float)(r) * (int)(t) / 100
    print("Simple Interest for given data : ", interest)


p = input("Enter Principal Amount :")
r = input("Enter Rate of interest : ")
t = input("Enter Time duration : ")
simple_interest(p, r, t)
