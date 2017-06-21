import numpy as np
import matplotlib.pyplot as plt

x, y = np.linspace(-5, 5, 20), np.linspace(-5, 5, 20)
u, v = np.meshgrid(x, y)
s = -u/v
plt.figure()
deg = np.arctan(s)
plt.quiver(u,v, np.cos(deg), np.sin(deg))
plt.show()
