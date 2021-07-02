import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-10,10,20)


def ricker(fz, t):
    f = 1 - 2*((np.pi*fz*t)**2)*(np.exp(np.pi*fz*t)**2)
    return f

fx = ricker(5, t)

#plt.figure(figsize=(8,8))
plt.plot(t,fx)
plt.show()

