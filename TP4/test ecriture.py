import numpy as np
import matplotlib.pyplot as plt

n = 50

x_k = 2*math.pi*k / n
y_k = math.cos(x_k)

plt.plot(x_k, y_k)