#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import preprocessing, metrics
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

import statsmodels.api as sm


# In[2]:


df=pd.read_csv('cleaning_data.csv')
df=df.drop(columns=["Unnamed: 0"])


# In[3]:


df


# In[18]:


copy_df=copy_df.drop(copy_df.index[0])
copy_df


# In[104]:


copy_df=df.drop(["Rank","Name","GP","MPG"],axis=1)


# In[ ]:





# In[105]:


copy_df.describe()


# In[106]:


X=copy_df.iloc[:,:-1]
y=copy_df.iloc[:,-1]


# In[107]:


xtrain,xtest,ytrain,ytest=train_test_split(X,y,random_state=0)


# In[108]:


xtest


# In[109]:


ytrain


# In[110]:


reg=LinearRegression(fit_intercept=False)
reg.fit(xtrain,ytrain)
y_pred=reg.predict(xtest)


# In[111]:


print(f"mse: {metrics.mean_squared_error(ytest,y_pred)}")
print(f"r^2: {metrics.r2_score(ytest,y_pred)}")


# In[112]:


reg.coef_


# In[113]:


for k,v in sorted(dict(zip(copy_df.columns,reg.coef_)).items(),key=lambda x:x[1],reverse=True):
    print(k,v)


# In[114]:


Comp = sm.OLS(y, X, data=df)

resultsb = Comp.fit()

print(resultsb.summary())


# In[115]:


df


# In[116]:


y_pred = reg.predict(X)
copy_df2 = pd.DataFrame({'Actual': y, 'Predicted': y_pred})
copy_df2["Difference"] = copy_df2["Actual"]-copy_df2["Predicted"]


# In[117]:


copy_df2


# In[ ]:




