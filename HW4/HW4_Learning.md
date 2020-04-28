# HW4 :　Black-Scholes Formula
陳又加｜經濟三｜B06303096 

## 利用B-S Model對歐式選擇權進行定價
### 參考課程投影片及 https://ch-hsieh.blogspot.com/2010/04/black-scholes-model.html
使用 B-S model 的一些假設

對於股價分布的假設 :
1. 股價服從連續複利 Log-normal 分布
2. 波動度(Volatility)為已知常數
3. 未來的股息已知

對於市場的假設 :
1. 無交易手續費用、無稅收
2. 證卷交易為連續進行
3. 短期無風險利率  r  為已知常數
4. 可以基於無風險利率執行 short sell or borrow
5. 不存在無風險套利機會 

### 使用公式
先從股票目前價格扣除發放股利的現值，再將除息後的現值代入公式計算call price及 put price。
![](https://i.imgur.com/s5SrYcm.png)

## 流程圖
![](https://i.imgur.com/Xn80JFB.png)

## 程式碼及運作結果
### code
```py
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

c = S_ExD * norm.cdf(d1) - X * math.exp(-r * maturity) * norm.cdf(d2)
p = X * (math.exp(-r * maturity)) * norm.cdf(-d2) - S_ExD * norm.cdf(-d1)

print("call price : %.3f" %c)
print("put price : %.3f" %p)
```
### Input
![](https://i.imgur.com/jqoCftb.png)

### Output
![](https://i.imgur.com/ZfQjj1m.png)
