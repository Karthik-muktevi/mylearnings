#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np

a,b,c = map(int,input().split())

a1 = np.array([input().split() for i in range(a)],dtype='int')
a2 = np.array([input().split() for i in range(b)],dtype='int')

print(np.concatenate((a1,a2)))


# In[ ]:




