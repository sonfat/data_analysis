#-*- coding:utf-8 -*-

import pandas as pd

catering_sale = '../data/catering_sale.xls'
data = pd.read_excel(catering_sale, index_col=u'日期')
# print data[u'销量']>1000 返回值为bool
data = data[(data[u'销量']>400) & (data[u'销量']<5000)]
statics = data.describe() #数据基本统计量

#极差
statics.loc[u'极差'] =  statics.loc['max'] - statics.loc['min']
#变异系数   标准差/均值  在进行数据统计分析时，如果变异系数大于15%，则要考虑该数据可能不正常，应该剔除。
statics.loc[u'变异系数'] = statics.loc['std'] / statics.loc['mean']
#四分位区间
statics.loc[u'四分位区间'] = statics.loc['75%'] - statics.loc['25%']

print statics