print("本金(萬元) : ")
c = int(input()) * 10000  # c: 本金

print("期數(年) : ")
n = int(input()) * 12   # n: 期數

print("年利率(%) : ") 
r = float(input()) * 0.01 / 12  # r: 利率


result = [] # result: 試算結果清單
cn = round(c / n)   # cn: 每期攤還本金
cic = 0  # cic: 本金利息累計
ic = 0  # ic: 利息累計
ctp = c  # ctp: 剩餘待還本金


for i in range(n) :

    inow = round(ctp * r)   # inow: 本期利息
    cic += (cn + inow)
    ic += inow
    ctp -= cn
    result.append([cn, inow, cic])


inow = round(ctp * r)
cic += (ctp + inow)
ic += inow
result.append([ctp, inow, cic])
   
    
for j in range(n) :
    print("第" + str(j + 1) + "期",
          "本金(元) : " + str(result[j][0]), 
          "利息(元) : " + str(result[j][1]),
          "本金利息累計 : " + str(result[j][2]))
print("全部利息 : " + str(ic))