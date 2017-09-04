def computepay(h, r):
    if h>40:
        x=(h*r)+(h-40)*(r*0.5)
    else:
        x=(h*r)
    return x

hrs = input("Enter number of hours: ")
rate = input("Enter rate: ")
h=float(hrs)
r=float(rate)

p = computepay(h, r)
print(p)
