# HW1: 完成本金平均攤還試算
陳又加｜經濟三｜B06303096
- 參考 https://ttc.scu.org.tw/memdca1.htm

# 流程圖
![](https://i.imgur.com/NoVNW6P.png)

# 學習歷程

## 本金平均攤還法是將本金平均在貸款期間償還，每期償還的本金均相同，而每期所攤還的利息卻因累積未攤還之本金逐漸減少而減少，因此，每期所攤還的本利和會越來越少。
- (參考 https://ttc.scu.org.tw/memdca1.htm)

## 試算結果主要分為3個部分 :
1. 每期攤還本金(元)	
2. 每期攤還利息(元)
3. 本金利息累計(元)

## 錯誤修正
- 第一次按流程圖寫完程式，發現未對小數點做處理
![](https://i.imgur.com/VQfy8bk.png)

- 第二次在計算攤還本金及利息時使用round()將小數點四捨五入到個位
- 未考慮到最後一期攤還本金金額不同，因此數字仍有誤
![](https://i.imgur.com/JZIqxJS.png)

- 將最後一期的數字單獨處理，得到正確的結果
![](https://i.imgur.com/TwYOwOn.png)
