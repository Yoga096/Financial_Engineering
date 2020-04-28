from scipy.stats import norm
import math

S = float(input("現在價格 : "))
X = float(input("履約價格 : "))
A = float(input("波動度(年) : "))
r = float(input("無風險年利率(%) : ")) * 0.01
maturity = int(input("到期(月) : ")) / 12

dividend = []
dividend_value = 0
dividend_n = int(input("除息次數 : "))
for i in range(dividend_n) :
    print("第", i+1, "次除息")
    dividend.append([int(input("時間(月) : "))])
    dividend[i].append(float(input("金額 : ")))
    d_value_now = dividend[i][1] * (math.exp(-r * (dividend[i][0] / 12)))
    dividend_value += d_value_now

S_ExD = S - dividend_value

d1 = (math.log(S_ExD /X) + (r + (A**2)/2) * maturity) / (A * (maturity**0.5))
d2 = d1 - (A * (maturity**0.5))

p = X * (math.exp(-r * maturity)) * norm.cdf(-d2) - S_ExD * norm.cdf(-d1)
c = S_ExD * norm.cdf(d1) - X * math.exp(-r * maturity) * norm.cdf(d2)

print("put price : %.3f" %p)
print("call price : %.3f" %c)