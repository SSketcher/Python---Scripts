import numpy as np 
import matplotlib.pyplot as plt

def logisticMap(generations = 20, growth_rate = 1, initial = 0.5):
    population = [initial]
    for X in range(generations-1):
        X = population[-1]
        X = growth_rate * X * (1 - X)
        population.append(X)
    return population


rates = np.linspace(0.5, 4, 8)
populations = []

for rate in rates:
    populations.append(logisticMap(30, rate))

X = np.linspace(0, 30 , 30)

for i in range(len(rates)):
    plt.plot(X, populations[i], label = str(rates[i]))
plt.title('Logistic model')
plt.xlabel('Generations')
plt.ylabel('Population')
plt.legend(loc = 'right')
plt.xlim(left = 0, right = 30)
plt.savefig('Logistic_model.png', dpi = 500)
plt.show()


rates = np.linspace(0, 4, 4000)
populations = []

for rate in rates:
    populations.append(logisticMap(200, rate))


for i in range(len(rates)):
    Y = populations[i][100:]
    X = np.ones(len(Y)) * rates[i]
    plt.plot(X,Y, '.', color = 'black', markersize = 0.2)
plt.title('Bifurcation Diagram')
plt.xlabel('Growth rate')
plt.ylabel('Population')
plt.xlim(left = 0, right = rates[-1])
plt.savefig('bifurcation _diagram.png', dpi = 500)
plt.show()