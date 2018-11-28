import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def list_productor(mean, dis, number):
    return np.random.normal(mean, dis*dis, number)

list1 = list_productor(8531, 956, 100)
list2 = list_productor(8631, 656, 100)
list3 = list_productor(8731, 1056, 100)
list4 = list_productor(8831, 756, 100)

data = pd.DataFrame({"Hausdorff":list1,
                    "City-block":list2,
                     "Wasserstein":list3,
                     "KL-divergence":list4
})
data.boxplot()
plt.ylabel("ARI")
plt.xlabel("Dissimilarity Measures")
plt.show()