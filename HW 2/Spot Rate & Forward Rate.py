import math
from pandas.core.frame import DataFrame

### spot rate

r = int(input("Duration of spot rate(years) : \n"))
print("Price of", r, "year unit zero-coupon bond : ")
P = float(input())

y = (P ** (-1 / r) - 1) * 100
Y = (-(r ** -1) * math.log(P)) * 100

print(r, " year spot rate of interest : ", "%.2f" %y, "%", sep="")
print(r, " year spot force of interest : ", "%.2f" % Y, "%\n", sep="")

### forward rate

t = int(input("Time due for the bedinning of forward rate(years) : \n"))
r = int(input("Duration of forward rate(years) : \n"))
print("Price of", r, "years unit zreo coupon bond : ")
p0 = float(input())
print("Price of", r + t, "years unit zero coupon bond : ")
p1 = float(input())

f = ((p0 / p1) ** (1 / r)) - 1
F = math.log(1 + f)
f = round(f, 4)
F = round(F, 4)

print(r, "year forward rate of interest beginning", t, "years from now :", "%.2f" %(f * 100) + "%")
print(r, "year forward force of interest beginning", t, "years from noe :", "%.2f" %(F * 100) + "%\n")

### forward rate table

price_all = []
for i in range(r + t + 1) :
    print("Price of", i, "th years : ")
    price_all.append(float(input()))

Forward = []
for i in range(r + t + 1) :
    x = []
    for j in range(r + t + 1) :
        if j < i : x.append("-") 
        elif j == i : x.append(0)
        else :
            fx = ((price_all[i] / price_all[j]) ** (1 / j)) - 1
            fx = round(fx, 4)
            x.append(fx)

    Forward.append(x)

Forward = DataFrame(Forward)
print(Forward)
