# HW3 :　選擇權二元定價模型
陳又加｜經濟三｜B06303096 


## Binomial Pricing Model
### 參考課程投影片及 https://ch-hsieh.blogspot.com/2014/04/binomial-pricing-model-1.html
> 考慮市場為無套利機會(No-Arbitrage opportunity)的市場，則我們可以建構一組能產生與選擇權相同的 payoff 的投資組合。因為既然 payoff 相同則其價值必須相同(由無套利機會假設兩者等價)。故此我們便可計算選擇權的(合理)價格。

### 使用公式
> 根據股票可能上漲或下跌的幅度，計算出到期後選擇權可能的 payoff，再以此回推選擇權今日的合理價格。當期的選擇權價格可經由下一期的價格期望值折回現值求得，回推至第 0 期的價格即為題目所求之選擇權價格。
![](https://i.imgur.com/36r3i2y.png)
 

## 流程圖
![](https://i.imgur.com/Bq8Vaif.png)


## 程式碼及運作結果
### Stock Price
```py
import pandas as pd
import math

S = float(input("目前股價 : "))
X = float(input("履約價格 : "))
u = float(input("上漲幅度 : "))
d = float(input("下跌幅度 : "))
r = float(input("無風險利率(%) : ")) * 0.01
n = int(input("期數 : "))
R = round(math.exp(r), 1)
print("無風險報酬 : ", R)
p = (R - d)/(u - d)


### 計算 stock price tree
s = [] 
for i in range(n + 1) :
    s.append([])
    for j in range(i + 1) :
        SP = S * (u ** j) * (d ** (i-j))
        s[i].append(SP)
```
![](https://i.imgur.com/uapwPhP.png)

### Probability
```py
prob = [[1.0], [p, round(1-p, 3)]] 
for i in range(2, n + 1) :
    prob.append([])
    for j in range(1) :
        prob[i].append(round(p ** i, 3))
    for j in range(1, i) :
        prob[i].append(round((prob[i-1][j-1] * (1-p)) + (prob[i-1][j] * p), 3))
    for j in range(i, i+1) :
        prob[i].append(round((1-p) ** i, 3))
```
![](https://i.imgur.com/ffrP54y.png)

### Call and Put Price
```py
### 計算 call price tree
c = [] 
for i in range(n + 1) :
    c.append([])
    for j in range(i + 1) :
        if s[i][j] - X >= 0 :
            c[i].append(s[i][j] - X)
        else :
            c[i].append(0.0)

for i in range(n-1, -1, -1) :
    for j in range(i + 1) :
        c[i][j] = round((p * c[i+1][j+1] + (1-p) * c[i+1][j])/R, 3)

c = pd.DataFrame(c)
call_price = c.T


### 計算 put price tree
put = [] 
for i in range(n + 1) :
    put.append([])
    for j in range(i + 1) :
        if X - s[i][j] >= 0 :
            put[i].append(X - s[i][j])
        else :
            put[i].append(0)

for i in range(n-1, -1, -1) :
    for j in range(i + 1) :
        put[i][j] = round(((p) * put[i+1][j+1] + (1-p) * put[i+1][j])/R, 3)

put = pd.DataFrame(put)
put_price = put.T
```
![](https://i.imgur.com/4Vbf40V.png)
