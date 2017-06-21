import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(y,x):
    return x+1-y
xy = np.array([5, 0])
x = np.linspace(-5, 5, 50)
solution = odeint(f, xy, x)
figure = plt.figure()
plt.plot(x, solution)
for i in np.arange(-5, 6, 1):
    if i !=1:
        y = x+1-i
        plt.plot(x, y)
        plt.quiver(x, y, np.cos(np.arctan(i)), np.sin(np.arctan(i)), np.ones(30)*np.arctan(i))
plt.quiver(x, x, np.cos(np.arctan(1.)), np.sin(np.arctan(1.)))
plt.xlabel('x')
plt.ylabel('y')

plt.show()
