#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import time 
import os       
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from datetime import datetime, date


# In[22]:


df=pd.read_csv('first_data.csv')


# In[23]:


copy_df = df.copy()


# In[24]:


copy_df


# In[25]:


del copy_df['Unnamed: 0']


# In[38]:


copy_df =copy_df.replace(0, np.nan)
copy_df = copy_df.dropna(thresh=19)
copy_df=copy_df.dropna(subset=['Weight'])
copy_df


# In[41]:


copy_df=copy_df.replace(np.nan,0)


# In[40]:


copy_df.to_csv('cleaning_data.csv')


# In[ ]:




