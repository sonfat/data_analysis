import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# x = np.random.randn(1000)
x = [1,2,3]
# print x
plt.hist(x,4)
plt.show()
