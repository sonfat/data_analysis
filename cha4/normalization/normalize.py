import pandas as pd
import numpy as np

spl = '============================================================================================'

data_file = 'normalization_data.xls'
# data = pd.read_excel(data_file)

def min_max_normalize(file):
    data = pd.read_excel(file, header=None)
    result = (data-data.min()) / (data.max()-data.min())
    return  result

def zero_aver_normalize(file):
    data = pd.read_excel(file, header=None)
    result = (data - data.mean()) / data.std()
    return result

def point_normalize(file):
    data = pd.read_excel(file, header=None)
    result = data/10**np.ceil(np.log10(data.abs().max()))
    return result

if __name__ == '__main__':
    min_max = min_max_normalize(data_file)
    zero_aver = zero_aver_normalize(data_file)
    point = point_normalize(data_file)
    print min_max
    print spl
    print zero_aver
    print spl
    print point