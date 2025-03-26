import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# total population
N = 1000
# infection probability
beta = 0.3
# recover probability
gamma = 0.05
# initial infected population
I0 = 1

# set the fiture
plt.figure(figsize=(6, 4), dpi=150)

# loop for different vaccination rate
for i in range(11):
    steps = 1000
    V_percentage = i * 0.1
    V = N * V_percentage # vaccated population
    S0 = N - I0 - V # suspectible population
    R0 = 0 # recovered population
    S = np.zeros(steps + 1) # creat a tuple to record the data of infected population
    I = np.zeros(steps + 1)
    R = np.zeros(steps + 1)
    S[0], I[0], R[0] = S0, I0, R0

    # loop for the infection times
    for t in range(steps):
        dR = np.sum(np.random.choice(range(2), int(I[t]), p=[1 - gamma, gamma]))
        dI0 = np.sum(np.random.choice(range(2), int(S[t] + V), p=[1 - beta * I[t] / N, beta * I[t] / N]))
        dV = np.sum(np.random.choice(range(2), int(V), p=[1 - beta * I[t] / N, beta * I[t] / N]))
        dI = dI0 - dV

        # set the value to the variables and make sure the values are bigger than 0
        S[t + 1] = max(0, S[t] - dI)
        I[t + 1] = max(0, I[t] + dI - dR)
        R[t + 1] = max(0, R[t] + dR)

    color_index = int(np.linspace(0, len(cm.viridis.colors) -1, 11)[i])
    plt.plot(I, label=f'{V_percentage * 100}%', color=cm.viridis(color_index))

# plot the fiture
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.show()