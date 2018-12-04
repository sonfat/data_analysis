import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
y1 = np.cos(x)
plt.plot(x, y1, '-')
plt.plot(x, y, 'bp--')
plt.show()