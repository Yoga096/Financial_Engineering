import math

t = int(input("Duration of spot rate(years) : \n"))
print("Price of", t, "year unit zero-coupon bond : ")
P = float(input())

y = (P ** (-1 / t) - 1) * 100
Y = (-(t ** -1) * math.log(P)) * 100

print(t, " year spot rate of interest : ", "%.2f" %y, "%", sep="")
print(t, " year spot force of interest : ", "%.2f" % Y, "%", sep="")