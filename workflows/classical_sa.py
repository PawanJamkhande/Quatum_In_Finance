import random
import numpy as np

def classical_solver(Q, steps=1000):
    N = Q.shape[0]
    x = np.random.randint(0, 2, size=N)

    def energy(x):
        return x @ Q @ x

    best_x = x.copy()
    best_energy = energy(x)

    for _ in range(steps):
        i = random.randint(0, N-1)
        x_new = x.copy()
        x_new[i] = 1 - x_new[i]

        if energy(x_new) < best_energy:
            best_x = x_new
            best_energy = energy(x_new)
            x = x_new

    return best_x, best_energy
