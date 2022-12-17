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
def read_sk_dataset(loaded_dataset):
    """Read dataset from sk datasets module and return dataframe.

    Parameters
    ----------
    loaded_dataset : sklearn.utils._bunch.Bunch
        dataset loaded from sklearn.datasets, e.g. datasets.load_iris()
    """
    df = pd.DataFrame(data=np.c_[loaded_dataset['data'],
                                 loaded_dataset['target']],
                      columns=loaded_dataset['feature_names'] + ['target'])
    return df


# In[6]:
new_dataset = datasets.load_iris()
df_iris = read_sk_dataset(new_dataset)


# In[7]:
df_iris.shape


# In[8]:
df_iris.head(10)
