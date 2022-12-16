# In[1]:
# Some Important Markdown


# In[2]:
"""Notebook for loading iris dataset """


# In[3]:
import numpy as np
import pandas as pd
from sklearn import datasets


# In[4]:
# Less important markdown
# That uses two cells


# In[5]:
iris = datasets.load_iris()
df_iris = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                       columns=iris['feature_names'] + ['target'])


# In[6]:
df_iris.head(10)
