print("本金(萬元) : ")
c = int(input()) * 10000

print("期數(年) : ")
n = int(input()) * 12 

print("年利率(%) : ") 
r = float(input()) * 0.01 / 12 


result = []
cn = round(c / n)
cic = 0 
ic = 0
ctp = c


for i in range(n-1) :

    inow = round(ctp * r)
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