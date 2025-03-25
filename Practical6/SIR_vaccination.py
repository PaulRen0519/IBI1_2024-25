import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


# 定义SIR模型模拟函数
def simulate_SIR(N, V_percentage, I0, beta, gamma, steps=1000):
    V = N * V_percentage
    S0 = N - I0 - V
    R0 = 0
    S = np.zeros(steps + 1)
    I = np.zeros(steps + 1)
    R = np.zeros(steps + 1)
    S[0], I[0], R[0] = S0, I0, R0

    for t in range(steps):
        dR = np.sum(np.random.choice(range(2), int(I[t]), p=[1 - gamma, gamma]))
        dI0 = np.sum(np.random.choice(range(2), int(S[t] + V), p=[1 - beta * I[t] / N, beta * I[t] / N]))
        dV = np.sum(np.random.choice(range(2), int(V), p=[1 - beta * I[t] / N, beta * I[t] / N]))
        dI = dI0 - dV

        S[t + 1] = max(0, S[t] - dI)
        I[t + 1] = max(0, I[t] + dI - dR)
        R[t + 1] = max(0, R[t] + dR)

    return I


# 总人数
N = 1000
# 感染概率
beta = 0.3
# 恢复概率
gamma = 0.05
# 初始感染人数
I0 = 1

# 图形设置
plt.figure(figsize=(8, 6), dpi=150)

# 循环不同的疫苗接种比例
for i in range(11):
    V_percentage = i * 0.1
    infected = simulate_SIR(N, V_percentage, I0, beta, gamma)
    color_index = int(np.linspace(0, len(cm.viridis.colors) - 1, 11)[i])
    plt.plot(infected, label=f'{V_percentage * 100}%', color=cm.viridis(color_index))

plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.show()