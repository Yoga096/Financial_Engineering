# HW2 : 計算市場債券報價中的 YTM、Spot Rate、Forward Rate 以及建立 Forward Rate 對照表
陳又加｜經濟三｜B06303096 <br>
<br>
# YTM
## 參考 :<br>
1. https://www.calkoo.com/en/ytm-calculator <br>
2. https://fizzbuzzer.com/wp-content/uploads/2017/05/bonds-ytm-cashflow-pv.png

## 流程圖
![](https://i.imgur.com/kzAFtHg.png)

## 修正歷程
> 一開始想以求方程式解的方式得出答案，但多次嘗試失敗。<br>
參考網路上的做法，改以調整逼近的方式求解。

> 一開始按網路上的示範，ytm每次的調整幅度設為0.0001，但與作業的參考網站所給數字有落差。<br>
後來將調整幅度改為0.000001，雖然程式運作時間較久但得出的數字與參考網站相符合。

## 運作結果
![](https://i.imgur.com/lQN2Hn5.png)

# Spot rate & Forward rate
## 參考 :<br>
1. https://www.trignosource.com/finance/spot%20rate.html#Calculator
2. https://www.trignosource.com/finance/Forward%20rate.html#Calculator

## 流程圖
![](https://i.imgur.com/bqPs3FA.png)

## 運作結果
![](https://i.imgur.com/JWzOxbB.png)

# Forward table
## 流程圖
![](https://i.imgur.com/X7EfDHz.png)

## 修正歷程
> 一開始i跟j的設定相反，導致程式錯誤。表格中沒有數字的部分也未做適當處理。
將表格分成右上、對角線、左下3部分分別處理。

## 運作結果
![](https://i.imgur.com/yjcJyeZ.png)
