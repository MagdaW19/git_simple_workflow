# In[1]:
import numpy as np 
import pandas as pd
from sklearn import datasets


# In[2]:
iris = datasets.load_iris()
df_iris = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])



# In[3]:
df_iris.head(20)


# In[4]:
df_iris.describe()


# In[5]:
print('notebook')


# In[6]:
print('this is a second notebook')
