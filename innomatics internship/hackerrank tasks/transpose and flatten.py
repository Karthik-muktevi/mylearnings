#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np

a,b = map(int,input().split())
l=[]
for i in range(a):
    m = list(map(int,input().split()))
    l.append(m)
    
l1 = np.array(l)
print(np.transpose(l1))
print(l1.flatten())


# In[ ]:




