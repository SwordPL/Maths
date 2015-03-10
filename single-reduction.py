import numpy as np


def fs(x, r):  # Function counting in single precision
    x = np.float32(x)
    r = np.float32(r)
    return r * x * (1 - x)


for x in np.linspace(0, 1, 100):
    iter = 0
    ox = x
    while x > np.finfo(np.float32).eps:  # While x is bigger than epsilon of the float32
        x = fs(x, 4)  # Iterate
        iter += 1
    print(ox, iter)

