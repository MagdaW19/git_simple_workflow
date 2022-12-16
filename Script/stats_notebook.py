# In[1]:
"""Notebook to read iris data and describe stats"""


# In[2]:
import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt


# In[3]:
dataset = datasets.load_iris()
df_data = pd.DataFrame(data=np.c_[dataset['data'], dataset['target']],
                       columns=dataset['feature_names'] + ['target'])


# In[4]:
df_data.plot()
plt.show()
