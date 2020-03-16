### 本金平均攤還試算

### 輸入本金、期數及年利率

print("本金(萬元) : ")
c = int(input()) * 10000
# 計算本金 * 萬

print("期數(年) : ")
n = int(input()) * 12 
# 計算總期數

print("年利率(%) : ") 
r = float(input()) * 0.01 / 12 
# 計算月利率

result = [] # 試算結果清單
cp = round(c / n) # 每期攤還本金 (四捨五入到個位)
cic = 0 # 本金利息累計



### 試算本金平均攤還

for i in range(n-1) :
# 計算 1 ~ 倒數第2期金額

    result.append([i + 1, round(cp), round((c * r))])
    # 在清單中加入期數、每期攤還本金、本期利息 (四捨五入到個位)
    
    cic += round(cp + (c * r))
    # 計算本金利息累計 (四捨五入到個位)

    c -= cp
    # 計算剩餘本金

    result[i].append(round(cic))
    # 在清單中加入本期為止本金利息累計 (四捨五入到個位)


# 計算最後一期金額 (四捨五入到個位)
result.append([n, round(c), round((c * r))])
cic += round(c + (c * r))
result[n - 1].append(round(cic))



### 印出試算結果
    
for j in range(n) :
    print("第" + str(result[j][0]) + "期",
          "本金(元) : " + str(result[j][1]), 
          "利息(元) : " + str(result[j][2]),
          "本金利息累計 : " + str(result[j][3]))