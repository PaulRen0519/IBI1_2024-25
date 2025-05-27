# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

beta = 0.3
gamma = 0.05
# 0 for suspectible 
# 1 for infected 
# 2 for recovered
# make array of all suspectible population
population = np.zeros((100, 100))

# begain with a point of infected person
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# draw a heat map
fig, ax = plt.subplots(figsize = (6, 4), dpi = 150)
im = ax.imshow(population, cmap='viridis', interpolation='nearest')

cmap = cm.get_cmap('viridis', 3)
im = ax.imshow(population, cmap=cmap, interpolation='nearest', vmin=0, vmax=2)

# add the color
cbar = fig.colorbar(im, ticks=[0, 1, 2])
cbar.ax.set_yticklabels(['Susceptible', 'Infected', 'Recovered'])

# find the infected population
def infected_population(population):
    return np.where(population == 1)

# find the infect neighbours and change their values
def infected_neighbours(population):
    infected_rows, infected_cols = infected_population(population)
    rows, cols = population.shape

    # find the neighbours
    for r, c in zip(infected_rows, infected_cols):
        for i in range(max(0, r - 1), min(r + 2, rows)):
            for j in range(max(0, c - 1), min(c + 2, cols)):

                # change the values
                if population[i, j] == 0:
                    population[i, j] = np.random.choice(range(2), 1, p = [1 - beta, beta])[0]
                elif population[i, j] == 1:
                    population[i, j] += np.random.choice(range(2), 1, p = [1 - gamma, gamma])[0]
    return population

# set the loop and update the data to the fiture
for t in range(100):
    population = infected_neighbours(population)

    im.set_data(population)
    plt.pause(0.1)

