import numpy as np

# rewards = [1,2,3,4,5,6,7]
# gamma_1 = 0.9
# gammas = np.ones(len(rewards))*gamma_1
# gammas = np.array([gammas[i]**i for i in range(len(rewards))])
# print(gammas)
# vanilla = [np.sum((gammas*rewards)[:i+1]) for i in range(len(rewards))]


# print(vanilla)

x = [[1,3,4], [5,6,8], [0,12,3]]

for i in reversed(range(10)):
    print(i)