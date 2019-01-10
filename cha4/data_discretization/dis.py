#-*- coding: utf-8 -*-

import pandas as pd

data_file = 'discretization_data.xls'
data = pd.read_excel(data_file)
data = data[u'肝气郁结证型系数'].copy()
k = 4

d1 = pd.cut(data, k, labels=range(k))
print d1
w = [1.0 * i / k for i in range(k+1)]
# w = data.describe()