# In[1]:
"""Notebook to read iris data and describe stats"""


# In[2]:
import numpy as np
import pandas as pd
from sklearn import datasets


# In[3]:
def deduplicate_hash(markdown):
    """Remove duplicates # characters from text

    Parameters
    ----------
    markdown : str
       original text

    Returns
    -------
    str
        text with deduplicated #
    """
    return markdown.replace('#', '').replace('\n', '\n#')


# In[4]:
dataset = datasets.load_iris()
df_data = pd.DataFrame(data=np.c_[dataset['data'], dataset['target']],
                       columns=dataset['feature_names'] + ['target'])


# In[5]:
df_data.describe()
