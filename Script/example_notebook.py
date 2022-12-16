# In[1]:
"""Notebook for loading iris dataset """


# In[2]:
import numpy as np
import pandas as pd
from sklearn import datasets


# In[3]:
iris = datasets.load_iris()
df_iris = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                       columns=iris['feature_names'] + ['target'])


# In[4]:
df_iris.head(10)
