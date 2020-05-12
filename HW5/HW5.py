import numpy as np
import QuantLib as ql
import matplotlib.pyplot as plt


timestep = int(input("timestep : "))
forward_rate = float(input("年化利率(%) : ")) * 0.01
sigma = float(input("sigma值 : "))
length = float(input("到期時間(年) : "))
a = float(input("a值 : "))
num_paths = int(input("模擬次數 : "))
dt = float(input("dt : "))
S = float(input("股票目前價格 : "))
X = float(input("履約價格 : "))
r = float(input("無風險利率(%) : ")) * 0.01


np.random.seed(1)
day_count = ql.Thirty360()
todays_date = ql.Date(13, 5, 2020)

ql.Settings.instance().evaluationDate = todays_date
spot_curve = ql.FlatForward(todays_date, ql.QuoteHandle(ql.SimpleQuote(forward_rate)), day_count)
spot_curve_handle = ql.YieldTermStructureHandle(spot_curve)

hw_process = ql.HullWhiteProcess(spot_curve_handle, a, sigma)
rng = ql.GaussianRandomSequenceGenerator(ql.UniformRandomSequenceGenerator(timestep, ql.UniformRandomGenerator()))
seq = ql.GaussianPathGenerator(hw_process, length, timestep, rng, False)    



## 對 Hull White Model 模擬 Short Rate
def generate_paths(num_paths, timestep) :
    arr = np.zeros((num_paths, timestep+1))
    for i in range(num_paths) :
        sample_path = seq.next()
        path = sample_path.value()
        time = [path.time(j) for j in range(len(path))]
        value = [path[j] for j in range(len(path))]
        arr[i, :] = np.array(value)
    return np.array(time), arr


time, paths = generate_paths(num_paths, timestep)
for i in range(num_paths) :
    plt.plot(time, paths[i, :], lw = 0.8, alpha = 0.6)
plt.title("Short Rate")
plt.show()



## 將 Short Rate 帶入 Geometric Brownian Motion，r 換成 r(t) 模擬股價
def genBrownPath(T, mu, sigma, S0, dt) :
    SP = []
    n = len(mu)
    t = np.linspace(0, T, n)
    W = [0] + np.random.standard_normal(size = 1) 
    W = (W + np.random.standard_normal(size = 1)) * np.sqrt(dt)
    for i in range(len(time)) :
        SP.append(S0 * np.exp((float(mu[i] )- 0.5  *sigma**2) * float(time[i]) + sigma * W)) 
    plt.plot(t, SP, lw = 0.8, alpha = 0.6)
    plt.title("Stock Price")
    return SP

SP_paths = []
for i in range(num_paths) :
    SP_paths.append(genBrownPath(timestep, paths[i, :], sigma, S, dt))
plt.show()



## 對每一條 path 計算出到期日時的 PayOff
payoff = []
for i in range(num_paths):
    Px = SP_paths[i][-1]
    payoff.append(int(Px - X))
print("PayOff :", payoff)



## 對所有 Path 的 PayOff 進行期望值計算，並折現回 t=0 的時間點
## 計算出 Call Price & Put Price
c = []
p = []
for i in range(num_paths):
    df = 0
    for j in range(len(paths[i])):
        df += paths[i][j]
    df = np.exp(df * length / timestep)

    if SP_paths[i][-1] > X :
        c.append((SP_paths[i][-1] - X) / df)
    else :
        c.append(0)
    if X > SP_paths[i][-1] :
        p.append((X - SP_paths[i][-1]) / df)
    else:
        p.append(0)
        

print("call price :", "%.3f" %(np.mean(c)))
print("put price :", "%.3f" %(np.mean(p)))