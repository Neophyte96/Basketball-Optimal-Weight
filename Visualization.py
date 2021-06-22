#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency


# In[3]:


df= pd.read_csv("cleaning_data.csv")
df=df.drop(columns=["Unnamed: 0"])
df


# In[8]:


df['Games_Played'] = pd.cut(df['GP'],bins=[0,100,400,700,3000], labels=["0-100","100-400","400-700","700+"])
gp = df.groupby('Games_Played').size()
gp = df['Games_Played'].value_counts()
print(gp)
gp.plot.pie(autopct='%1.1f%%',shadow=True,startangle=90,explode=(0.05, 0.05,0.05,0.05),radius=1.5,figsize=(7,6),textprops={'fontsize':15})


# In[16]:


df['points_pergame'] = pd.cut(df['PPG'],bins=[0,5,10,20,35], labels=["0-5","5-10","10-20","20+"])
gp = df.groupby('points_pergame').size()
gp = df['points_pergame'].value_counts()
print(gp)
gp.plot.pie(autopct='%1.1f%%',shadow=True,startangle=90,explode=(0.05, 0.05,0.05,0.05),radius=1.5,figsize=(7,6),textprops={'fontsize':15})


# In[9]:


x =df["MPG"]
y= df["PPG"]


plt.scatter(x, y)
plt.show()


# In[10]:


sns.pairplot(df[['MPG','PPG', 'FGA', 'GP',"3PA"]])


# In[14]:


g = sns.catplot(
    x='MPG', 
    data =df,
    kind='boxen', 
    hue='PPG',
    palette=['#E74C3C', '#7FB3D5', '#27AE60'],
    height=7, 
    aspect=2,
    legend=False,
    ).set_axis_labels('MPG', 'PPG')


# In[17]:


df.info()


# In[18]:


df.describe()


# In[ ]:





# In[ ]:




