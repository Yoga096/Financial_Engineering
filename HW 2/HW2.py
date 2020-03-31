import math

def PV_new(FV, coupon, n, CR):
    
    PV_now = FV / math.pow((1 + CR), n)
    for i in range(1, n+1) :
        PV_now += coupon / math.pow(1 + CR, i)

    return PV_now

PV = float(input("Current Bond Price :"))
FV = float(input("Bond Par Value :"))
CR = float(input("Bond Coupon Rate (% p.a.) :"))
Y = int(input("Years to Maturity :"))
p = int(input("Payment  \n1 (Annually) \n2 (Semi-annually) \n4 (Quartely) :"))   

CR = CR * 0.01
n = Y * p         
coupon = FV * CR
ytm = CR
condition = True

while condition == True :
    
    if PV < FV :
        ytm += 0.0000001
    else :
        ytm -= 0.0000001

    PV_now = PV_new(FV, coupon/p, n, ytm/p)

    if PV < FV :
        condition = PV_now > PV
    else :
        condition = PV_now < PV

print("YTM : %.4f%%" % ((ytm / p) * 100.0))