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

day_count = ql.Thirty360()
todays_date = ql.Date(13, 5, 2020)
np.random.seed(1)

ql.Settings.instance().evaluationDate = todays_date
spot_curve = ql.FlatForward(todays_date, ql.QuoteHandle(ql.SimpleQuote(forward_rate)), day_count)
spot_curve_handle = ql.YieldTermStructureHandle(spot_curve)


hw_process = ql.HullWhiteProcess(spot_curve_handle, a, sigma)
rng = ql.GaussianRandomSequenceGenerator(ql.UniformRandomSequenceGenerator(timestep, ql.UniformRandomGenerator()))
seq = ql.GaussianPathGenerator(hw_process, length, timestep, rng, False)    


def generate_paths(num_paths, timestep):
    arr = np.zeros((num_paths, timestep+1))
    for i in range(num_paths):
        sample_path = seq.next()
        path = sample_path.value()
        time = [path.time(j) for j in range(len(path))]
        value = [path[j] for j in range(len(path))]
        arr[i, :] = np.array(value)
    return np.array(time), arr

time, paths = generate_paths(num_paths, timestep)
for i in range(num_paths):
    plt.plot(time, paths[i, :], lw = 0.8, alpha = 0.6)
plt.title("Hull-White Short Rate Simulation")
plt.show()








