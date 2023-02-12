import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return abs(x-2)-abs(x)

def g(x):
    return abs(x-2)

def h(x):
    return -abs(x)

x = np.linspace(-5, 15, 100)
print(type(x))
plt.plot(x, f(x))
plt.plot(x, g(x))
plt.plot(x, h(x))
#plt.scatter([0,1,2], [1,3,5])
#plt.scatter([0,1,2], [2,5,6])
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.show()
