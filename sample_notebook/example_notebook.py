## Example Notebook

import numpy as np 
import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()
df_iris = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])


df_iris.head(10)

print('notebook')

