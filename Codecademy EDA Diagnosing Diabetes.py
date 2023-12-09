#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np

diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data.head())


# In[11]:


print(diabetes_data.isnull().sum())


# In[12]:


print(diabetes_data.info())


# In[13]:


print(diabetes_data.describe())


# In[15]:


diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)


# In[16]:


print(diabetes_data.describe())


# In[17]:


print(diabetes_data.isnull().sum())


# In[18]:


print(diabetes_data[diabetes_data.isnull().any(axis=1)])


# In[19]:


print(diabetes_data.dtypes)


# In[20]:


print(diabetes_data.Outcome.unique())


# In[21]:


diabetes_data['Outcome'] = diabetes_data['Outcome'].str.replace('O', '0')


# In[29]:


diabetes_data['Outcome'] = diabetes_data['Outcome'].astype('int64')


# In[22]:


print(diabetes_data.Outcome.unique())


# In[31]:


print(diabetes_data.dtypes)


# In[ ]:




