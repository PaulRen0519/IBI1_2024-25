import numpy as np
import matplotlib.pyplot as plt

# set variables for each population
N = 1000  # total population
I0 = 1  # initial infected population
S0 = N - I0  # initial suspectible population
R0 = 0  # initial recovered population
beta = 0.3  # infection probability
gamma = 0.05  # recover probability
S = [S0]
I = [I0]
R = [R0]

# build up a loop for 1000 times
for t in range(1000):
    # recovered population equal to the product of infected population and gamma
    dR = np.sum(np.random.choice(range(2), I[t], p=[1 - gamma, gamma]))

    # infected population equal to the product of suspectible population and beta and the portion of infected population
    dI = np.sum(np.random.choice(range(2), S[t], p=[1 - beta * I[t] / N, beta * I[t] / N]))

    # add the data to the list
    S.append(S[t] - dI)
    I.append(I[t] + dI - dR)
    R.append(R[t] + dR)

    # ensure non-negative values
    S[-1] = max(0, S[-1])
    I[-1] = max(0, I[-1])
    R[-1] = max(0, R[-1])

print(S, I, R)

# plot the results
plt.figure(figsize = (6, 4), dpi = 150)
plt.plot(S, label='Susceptible')
plt.plot(I, label='Infected')
plt.plot(R, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('SIR Model')
plt.legend()
plt.savefig("SIR", format = "png")
plt.show()


