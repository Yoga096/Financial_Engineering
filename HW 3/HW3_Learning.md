# HW3 :　選擇權二元定價模型
陳又加｜經濟三｜B06303096 


## Binomial Pricing Model
### 參考課程投影片及 https://ch-hsieh.blogspot.com/2014/04/binomial-pricing-model-1.html
> 考慮市場為無套利機會(No-Arbitrage opportunity)的市場，則我們可以建構一組能產生與選擇權相同的 payoff 的投資組合。因為既然 payoff 相同則其價值必須相同(由無套利機會假設兩者等價)。故此我們便可計算選擇權的(合理)價格。

### 示意圖及公式
> 根據股票可能上漲或下跌的幅度，計算出到期後選擇權可能的 payoff，再以此回推選擇權今日的合理價格。
![](https://i.imgur.com/36r3i2y.png)
 

## 流程圖
![](https://i.imgur.com/Bq8Vaif.png)


## 程式碼及運作結果
![](https://i.imgur.com/FuSoUXU.png)
### Stock price tree
```
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

