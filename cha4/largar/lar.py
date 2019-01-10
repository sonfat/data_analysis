# -*- coding:utf-8 -*-

import pandas as pd
from scipy.interpolate import lagrange

#

input_file = 'catering_sale.xls'
output_file = 'result.xls'

data = pd.read_excel(input_file)
data[(data[u'销量']<400)|(data[u'销量']>5000)] = None
# print data
def test(s, n, k=5):
    y = s[list(range(n - k, n)) + list(range(n + 1, n + 1 + k))]
    return y

def ployinterp_colum(s, n, k=5):
    y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))]
    y = y[y.notnull()]
    return lagrange(y.index, list(y)) (n)

for i in data.columns:
    for j in range(len(data)):
        if(data[i].isnull())[j]:
            data[i][j] = ployinterp_colum(data[i],j)
data.to_excel(output_file)