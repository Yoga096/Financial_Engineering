import pandas as pd
import numpy as np
import copy
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

s = [] # stock price
for i in range(n + 1) :
    s.append([])
    for j in range(i + 1) :
        SP = S * (u ** j) * (d ** (i-j))
        s[i].append(SP)

prob = [[1.0], [p, round(1-p, 3)]] # probility
for i in range(2, n + 1) :
    prob.append([])
    for j in range(1) :
        prob[i].append(round(p ** i, 3))
    for j in range(1, i) :
        prob[i].append(round((prob[i-1][j-1] * (1-p)) + (prob[i-1][j] * p), 3))
    for j in range(i, i+1) :
        prob[i].append(round((1-p) ** i, 3))

c = [] # call price
for i in range(n + 1) :
    c.append([])
    for j in range(i + 1) :
        if s[i][j] - X >= 0 :
            c[i].append(s[i][j] - X)
        else :
            c[i].append(0)

for i in range(n-1, -1, -1) :
    for j in range(i + 1) :
        c[i][j] = round((p * c[i+1][j+1] + (1-p) * c[i+1][j])/R, 3)


print(s)
print(prob)
print(c)


