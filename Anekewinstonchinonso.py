#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


af = pd.read_csv("C:/Users/Chikelu Emmanuella/Downloads/FoodBalanceSheets_E_Africa_NOFLAG.csv")


# In[4]:


af


# In[6]:


af.groupby("Item")["Y2014", "Y2017"].sum()


# In[10]:


af.describe()


# In[12]:


af.isnull().sum()


# In[13]:


af.groupby("Element")["Y2014", "Y2015","Y2016","Y2017","Y2018"].sum()


# In[14]:


af.groupby("Element")["Y2014"].sum()


# In[17]:


af.groupby("Element")["Element", "Y2018"].sum()


# In[19]:


af.groupby("Area")[ "Y2018"].sum()


# In[33]:


af.groupby(["Area","Element"])["Y2018"].sum()


# In[ ]:




