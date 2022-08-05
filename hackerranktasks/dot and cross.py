#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy

a = int(input())

b =numpy.array([input().split() for i in range(a)],dtype='int')

c =numpy.array([input().split() for i in range(a)],dtype='int')
print(numpy.dot(b,c))


# In[ ]:




