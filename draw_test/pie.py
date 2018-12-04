import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

labels = 'Frogs','Hogs','Dogs','Logs'
sizes = [15,20,45,20]
colors = ['red','blue','yellow','pink']
explode = (0,0.1,0,0)
plt.pie(sizes, explode=explode, colors=colors, labels=labels, shadow=True, startangle=90, autopct='%1.1f%%')
plt.axis('equal')
plt.show()