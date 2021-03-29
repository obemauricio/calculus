import numpy as np
import matplotlib.pyplot as plt

n = 1000
def f(x):
    return x**2;
c = 10
x = np.linspace(-15, 15, num=n)

y = f(x)

fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()
ax.axhline(y=0, color='r',)
ax.axvline(x=0, color='r')
