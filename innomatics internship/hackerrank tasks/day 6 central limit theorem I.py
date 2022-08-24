#!/usr/bin/env python
# coding: utf-8

# In[52]:


import math

wt = int(input())
n = int(input())

mu = int(input())

sd = int(input())


# In[54]:


from scipy import stats


# In[55]:


z = (wt-n*mu)/15/n**0.5


# In[62]:


z


# In[61]:


round(stats.norm.cdf(z),4)


# In[ ]:




