#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x= pd.Series(np.exp(np.arange(20)))
x.plot(label=u'原始数据', legend=True)
plt.show()

x.plot(logy=True, label=u'对数数据', legend=True)
plt.show()