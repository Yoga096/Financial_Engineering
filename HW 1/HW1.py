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
ctp = c # 剩餘未還本金


### 試算本金平均攤還

for i in range(1, n) :
# 計算 1 ~ 倒數第2期金額

    inow = round(ctp * r) 
    # 計算本期利率
   
    cic += (cp + inow)
    # 計算本金利息累計 (四捨五入到個位)

    ctp -= cp
    # 計算剩餘本金

    result.append([cp, inow, cic])
    # 在清單中加入本期攤還本金、本期利息、本期為止本金利息累計 (四捨五入到個位)

inow = round(ctp * r)
cic += (ctp + inow)
result.append([ctp, inow, cic])
# 最後一期攤還剩餘本金、計算利息、本金利息累計


### 印出試算結果
    
for j in range(n) :
    print("第" + str(j + 1) + "期",
          "本金(元) : " + str(result[j][0]), 
          "利息(元) : " + str(result[j][1]),
          "本金利息累計 : " + str(result[j][2]))